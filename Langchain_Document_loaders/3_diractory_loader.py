from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader   # to load multiple files

loader=DirectoryLoader(
    path='books', 
    glob='*.pdf',                      # means all pdf
    loader_cls=PyPDFLoader
)

# docs=loader.load()
docs=loader.lazy_load()

#print(docs)

print(type(docs))   # list 

# print(len(docs))   # pages in pdf

# print(docs[0].page_content)
# print(docs[0].metadata)



for doc in docs: 
    print(doc.metadata)