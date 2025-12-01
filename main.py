import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 1. Inisialisasi Model
# Pastikan GEMINI_API_KEY atau GOOGLE_API_KEY sudah diatur di environment
try:
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.7)
except Exception as e:
    print(f"ERROR: Gagal menginisialisasi model. Pastikan API Key sudah diatur. Detail: {e}")
    exit()

# 2. Mendefinisikan Prompt Template
# Prompt template digunakan untuk memformat input pengguna agar sesuai untuk LLM
prompt = ChatPromptTemplate.from_messages([
    ("system", "Anda adalah asisten AI yang ramah dan membantu. Balaslah dengan bahasa Indonesia."),
    ("user", "{input}"),
])

# 3. Membuat Chain
# Chain (Rantai) menghubungkan prompt, model, dan output parser secara berurutan
# Ini adalah inti dari LangChain: Prompt -> LLM -> OutputParser
chain = prompt | llm | StrOutputParser()

# 4. Memanggil Chain (Inferensi)
user_input = "Jelaskan konsep dasar LangChain dalam satu paragraf."
print(f"Pertanyaan Pengguna: {user_input}\n")

# Chain.invoke menjalankan seluruh proses
response = chain.invoke({"input": user_input})

# 5. Menampilkan Hasil
print("--- Jawaban Gemini ---")
print(response)
print("-----------------------")

# Contoh output:
# Pertanyaan Pengguna: Jelaskan konsep dasar LangChain dalam satu paragraf.
#
# --- Jawaban Gemini ---
# LangChain adalah framework yang dirancang untuk membantu pengembang membangun aplikasi 
# yang didukung oleh Large Language Models (LLM) dengan merangkai berbagai komponen 
# seperti model itu sendiri, prompt template, output parser, dan alat-alat (tools) 
# lainnya menjadi sebuah "chain" (rantai). Konsep intinya adalah modularitas, 
# memungkinkan pengembang untuk menghubungkan LLM dengan sumber data eksternal, 
# memori, dan fungsi logika lainnya untuk menciptakan aplikasi yang lebih kompleks dan kontekstual.
# -----------------------