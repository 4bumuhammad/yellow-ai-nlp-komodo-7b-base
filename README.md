# Yellow-AI-NPL / komodo-7b-base

Original source : 
<pre>https://huggingface.co/Yellow-AI-NLP/komodo-7b-base</pre>

---

&nbsp;

## Model Card for Komodo-7B-Base

Komodo-7B-Base adalah large language model yang dikembangkan melalui pelatihan awal dan perluasan kosakata di atas Llama-2-7B-Base. Model ini dapat menangani bahasa Indonesia, bahasa Inggris, dan 11 bahasa daerah di Indonesia.

**Disclaimer**: Ini bukan model instruction-tuned , fine-tuning diperlukan untuk tugas downstream. Sebagai contoh, orang biasanya menggunakan dataset Alpaca untuk penyempurnaan lebih lanjut di atas model Llama-2-7B-Base. Oleh karena itu, tidak ada template yang cepat untuk model ini.

&nbsp;

**Model Details**

<div align="center">
    <img src="./gambar-petunjuk/ss_komodo_7b_base_001.png" alt="ss_komodo_7b_base_001" style="display: block; margin: 0 auto;">
</div> 

&nbsp;

**Model Description**

Rincian lebih lanjut dapat ditemukan dalam makalah kami https://arxiv.org/abs/2403.09362
- **Developed by**: Yellow.ai
- **Model type**: Decoder
- **Languages**: English, Indonesian, Acehnese, Balinese, Banjarese, Buginese, Madurese, Minangkabau, Javanese, Dayak Ngaju, Sundanese, Toba Batak, Lampungnese
- **License**: llama2

&nbsp;

**Usage Example**

Karena ini adalah model yang terjaga keamanannya, Anda harus masuk ke akun HF Anda sebelum menggunakan model ini. Di bawah ini adalah salah satu cara untuk melakukannya. Anda bisa mendapatkan Token HF dari profil Anda (Profile -> Settings -> Access Tokens)

```bash
    import huggingface_hub
    huggingface_hub.login("YOUR_HF_TOKEN")
```

Setelah Anda masuk, Anda dapat mulai mengunduh dan memuat model & tokenizer. Kami menulis fungsi decoding khusus untuk Komodo-7B, oleh karena itu kami perlu memberikan trust_remote_code = True. Kode juga dapat bekerja tanpa parameter ini, tetapi proses decoding tidak akan bekerja seperti yang diharapkan.

```bash
    import torch
    from transformers import AutoTokenizer, AutoModelForCausalLM

    device = "cuda:0" if torch.cuda.is_available() else "cpu"

    tokenizer = AutoTokenizer.from_pretrained("Yellow-AI-NLP/komodo-7b-base",trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained("Yellow-AI-NLP/komodo-7b-base",trust_remote_code=True)
    model = model.to(device)
```
Kemudian, Anda bisa mencoba menggunakan model ini.
```bash
    full_prompt = "Candi borobudur adalah"

    tokens = tokenizer(full_prompt, return_tensors="pt").to(device)
    output = model.generate(tokens["input_ids"], eos_token_id=tokenizer.eos_token_id)

    print(tokenizer.decode(output[0], skip_special_tokens=True))
    # Candi borobudur adalah candi yang terletak di Magelang, Jawa Tengah.
```

&nbsp;

### Technical Specifications
**Model Architecture and Objective**<br />

Komodo-7B is a decoder model using the Llama-2 architecture.

| **Parameter**   | **Komodo-7B** |
|-----------------|---------------|
| Layers          | 32            |
| d_model         | 4096          |
| head_dim        | 32            |
| Vocabulary      | 35008         |
| Sequence Length | 4096          |


&nbsp;

&nbsp;

&nbsp;

| **Organization** | **Model Name**             | **Indo MMLU** | **ID-EN** | **XCOPA-ID** | **Intent Classification** | **Colloquial Detection** | **NusaX-Senti** | **ID-Hate Speech** | **TydiQA-ID** |
|------------------|----------------------------|---------------|-----------|--------------|---------------------------|--------------------------|-----------------|--------------------|---------------|
| OpenAI           | GPT-3.5-turbo-0301         | 51.3          | 64.5      | 70.0         | 82.0                      | 64.1                     | 47.2            | 68.0               | 85.3          |
| OpenAI           | GPT-3.5-turbo-0613         | 52.7          | 66.8      | 88.2         | 84.0                      | 75.1                     | 63.3            | 63.7               | 86.4          |
| OpenAI           | GPT-3.5-turbo-1106         | 53.3          | 69.7      | 89.3         | 84.0                      | 64.2                     | 59.8            | 56.6               | 88.0          |
| OpenAI           | GPT-4-preview-1106         | 69.8          | 78.0      | 98.3         | 89.0                      | 92.7                     | 66.1            | 73.4               | 72.0          |
| Meta             | Llama-2-7B-Chat            | 30.4          | 45.6      | 41.5         | 57.0                      | 31.4                     | 2.9             | 41.3               | 11.7          |
| Meta             | Llama-2-13B-Chat           | 32.0          | 61.7      | 38.0         | 59.0                      | 31.1                     | 58.7            | 57.2               | 71.9          |
| Google           | Gemma-7B-it                | 37.4          | 73.6      | 57.7         | 77.1                      | 18.8                     | 44.2            | 54.8               | 73.3          |
| Mistral          | Mixtral-8x7B-v0.1-Instruct | 45.2          | 57.8      | 88.7         | 86.0                      | 41.1                     | 52.8            | 68.8               | 90.3          |


