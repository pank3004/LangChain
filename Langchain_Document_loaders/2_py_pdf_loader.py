from langchain_community.document_loaders import PyPDFLoader   # to load only text based pdf

loader=PyPDFLoader("sample.pdf")
docs=loader.load()


print(docs)

print(type(docs))   # list 

print(len(docs))   # pages in pdf

print(docs[0].page_content)    # page content of 1st page
print(docs[0].metadata)     # meta data of 1st page

