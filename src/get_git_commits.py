import git

repo = git.Repo('.', search_parent_directories=True)
print(repo.tree().blobs[0].mime_type)
#print(repo.tree().blobs[2].data_stream.read().decode())
"""
for item in repo.index.diff(None):
    print (item.a_path)
    print(item)
"""
# the below gives us all commits
repo.commit('create-samples')  # specify the branch
hcommit = repo.head.commit
#print(hcommit.diff())               # diff tree against index

print(hcommit.diff(None))         # diff tree against previous tree

for gg in hcommit.diff("HEAD~1"):
    print(gg.a_blob.data_stream.read().decode())
    # print(gg.change_type)
    # print(gg.a_rawpath.decode())
    # print(gg)
    # print(gg.b_rawpath.decode())

#print(hcommit.diff('HEAD~1')[0].b_blob.data_stream.read().decode())
#print(hcommit.diff(None) )            # diff tree against working tree

print(repo.git.log(p=True))
