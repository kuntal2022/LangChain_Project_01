import ast

# file read karo
with open(r"C:\Users\Neel\Desktop\Azure_open_ai\chat_boat\chat_history.txt", "r") as f:
    data = f.read()

# "chat_history = [...]" se sirf list nikalo
data = data.replace("chat_history = ", "").strip()

# string ko actual list banao
chat_history = ast.literal_eval(data)

print(chat_history)        # poori list
print(chat_history[0])     # pehla message
print(chat_history[0]["content"])  # content