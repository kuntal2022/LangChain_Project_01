from langchain_community.document_loaders import TextLoader 

loader = TextLoader(file_path= r"C:\Users\Neel\Desktop\Azure_open_ai\Loader\documnets_folders\circket_poem.text", encoding='utf-8' )

docs=loader.load()

print()
print("Type of the Documnet - List")
print(type(docs))
print("Type of the Documnet[0] - Document Class Object")
print(type(docs[0]))
print("Type of the Documnet[0].page_content - str")
print(type(docs[0].page_content))

print("Follow this documnet for more knowledge on Langchain")
print(r"https://docs.langchain.com/oss/python/langchain/install") 





