# &#127937; Python : usage example 

&nbsp;

Please be sure to agree to the terms of access to this repository.
<div align="center">
    <img src="../gambar-petunjuk/ss_komodo_7b_base_003.png" alt="ss_komodo_7b_base_003" style="display: block; margin: 0 auto;">
</div> 

&nbsp;

---

## &#x1F530; Begin

Creating Directories and File Structures

<pre>
    ❯ vim requirements.txt

        huggingface-hub
        torch==2.2.1
        transformers==4.40.2
</pre>

<pre>
    ❯ pwd
        /Users/.../&lt;project-name&gt;

    ❯ cd &lt;project-name&gt;

    ❯ python -m venv venv

    ❯ source ./venv/bin/activate

    ❯ pip install --no-cache-dir -r requirements.txt
</pre>

&nbsp;

List of installed packages.
<pre>
    ❯ pip list

        Package            Version
        ------------------ ---------
        certifi            2024.2.2
        charset-normalizer 3.3.2
        filelock           3.14.0
        fsspec             2024.5.0
        huggingface-hub    0.23.1
        idna               3.7
        Jinja2             3.1.4
        MarkupSafe         2.1.5
        mpmath             1.3.0
        networkx           3.3
        numpy              1.26.4
        packaging          24.0
        pip                22.0.4
        PyYAML             6.0.1
        regex              2024.5.15
        requests           2.32.2
        safetensors        0.4.3
        setuptools         58.1.0
        sympy              1.12
        tokenizers         0.19.1
        torch              2.2.1
        tqdm               4.66.4
        transformers       4.40.2
        typing_extensions  4.12.0
        urllib3            2.2.1
</pre>

&nbsp;

Code
<pre>
    ❯ vim hf-login.py
        . . .

        import huggingface_hub

        huggingface_hub.login("&#x2774;CREDENTIAL_TOKEN&#x2775;") 
</pre>

<pre>
    ❯ vim model-prompt.py
        . . .

            import torch
            from transformers import AutoTokenizer, AutoModelForCausalLM

            device = "cuda:0" if torch.cuda.is_available() else "cpu"

            tokenizer = AutoTokenizer.from_pretrained("Yellow-AI-NLP/komodo-7b-base",trust_remote_code=True)
            model = AutoModelForCausalLM.from_pretrained("Yellow-AI-NLP/komodo-7b-base",trust_remote_code=True)
            model = model.to(device)

            # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

            full_prompt = "Candi borobudur adalah"

            tokens = tokenizer(full_prompt, return_tensors="pt").to(device)
            output = model.generate(tokens["input_ids"], eos_token_id=tokenizer.eos_token_id)

            print(tokenizer.decode(output[0], skip_special_tokens=True))
            # Candi borobudur adalah candi yang terletak di Magelang, Jawa Tengah.        
</pre>

## &#x1F3C3; Run

