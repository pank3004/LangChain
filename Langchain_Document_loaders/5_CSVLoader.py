from langchain_community.document_loaders import CSVLoader  # to load csv file


loader=CSVLoader("day.csv")
docs=loader.load()


print(docs)

print(type(docs))   # list 

print(len(docs))   # pages in pdf

print(docs[0].page_content)
print(docs[0].metadata)

print(docs[1])

