import tensorflow as tf
import numpy as np
import pandas as pd
import os

TH = os.environ.get("threshold")

TESTS_LIST = ["test_update_person_name", "test_get_car_owner"]

TRAIN_DATA = "./data/train/sample.csv"
GLOVE_EMBEDDING = "./data/glove.6B/glove.6B.50d.txt"

train = pd.read_csv(TRAIN_DATA)

train["commit_text"].fillna("fillna")

x_train = train["commit_text"].str.lower()
y_train = train[["test_update_person_name", "test_get_car_owner"]].values

max_words = 50
max_len = 50

embed_size = 50

tokenizer = tf.keras.preprocessing.text.Tokenizer(num_words=max_words, lower=True)

tokenizer.fit_on_texts(x_train)

x_train = tokenizer.texts_to_sequences(x_train)

x_train = tf.keras.preprocessing.sequence.pad_sequences(x_train, maxlen=max_len)

embeddings_index = {}

with open(GLOVE_EMBEDDING, encoding='utf8') as f:
    for line in f:
        values = line.rstrip().rsplit(' ')
        word = values[0]
        embed = np.asarray(values[1:], dtype='float32')
        embeddings_index[word] = embed

word_index = tokenizer.word_index

num_words = min(max_words, len(word_index) + 1)

embedding_matrix = np.zeros((num_words, embed_size), dtype='float32')

for word, i in word_index.items():

    if i >= max_words:
        continue

    embedding_vector = embeddings_index.get(word)

    if embedding_vector is not None:
        embedding_matrix[i] = embedding_vector

input = tf.keras.layers.Input(shape=(max_len,))

x = tf.keras.layers.Embedding(50, embed_size, weights=[embedding_matrix], trainable=False)(input)

x = tf.keras.layers.Bidirectional(tf.keras.layers.GRU(128, return_sequences=True, dropout=0.1,
                                                      recurrent_dropout=0.1))(x)

x = tf.keras.layers.Conv1D(64, kernel_size=3, padding="valid", kernel_initializer="glorot_uniform")(x)

avg_pool = tf.keras.layers.GlobalAveragePooling1D()(x)
max_pool = tf.keras.layers.GlobalMaxPooling1D()(x)

x = tf.keras.layers.concatenate([avg_pool, max_pool])

preds = tf.keras.layers.Dense(2, activation="sigmoid")(x)

model = tf.keras.Model(input, preds)

model.summary()

model.compile(loss='binary_crossentropy', optimizer=tf.keras.optimizers.Adam(lr=1e-3), metrics=['accuracy'])

batch_size = 5

checkpoint_path = "training_1/cp.ckpt"
checkpoint_dir = os.path.dirname(checkpoint_path)

cp_callback = tf.keras.callbacks.ModelCheckpoint(checkpoint_path,
                                                 save_weights_only=True,
                                                 verbose=1)

callbacks = [
    tf.keras.callbacks.EarlyStopping(patience=5, monitor='val_loss'),
    tf.keras.callbacks.TensorBoard(log_dir='./logs'),
    cp_callback
]

model.fit(x_train, y_train, validation_split=0.2, batch_size=batch_size,
          epochs=1, callbacks=callbacks, verbose=1)

latest = tf.train.latest_checkpoint(checkpoint_dir)

model.load_weights(latest)
yt = tokenizer.texts_to_sequences(['self.name'])
yt = tf.keras.preprocessing.sequence.pad_sequences(yt, maxlen=max_len)

predictions = model.predict(np.expand_dims(yt[0], 0))

print(tokenizer.sequences_to_texts([yt[0]]))

# print(y_train[4])

print(predictions)

tests_should_run = []
index = 0

for item in predictions[0]:
    if item >= float(TH):
        tests_should_run.append(TESTS_LIST[index])
    index += 1
print(f"Threshold: {str(TH)} ")
print('Tests should run: ' + '\33[34m' + str(tests_should_run) + '\033[0m')
