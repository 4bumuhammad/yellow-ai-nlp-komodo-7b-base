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
        huggingface-hub    0.23.2
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

Code &#x270E;
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

<pre>
    ❯ python3 hf-login.py

        The token has not been saved to the git credentials helper. Pass `add_to_git_credential=True` in this function directly or `--add-to-git-credential` if using via `huggingface-cli` if you want to set the git credential as well.
        Token is valid (permission: fineGrained).
        Your token has been saved to /Users/powercommerce/.cache/huggingface/token
        Login successful
</pre>

&nbsp;

Check the result files after running the script command 
<pre>
    ❯ du -sch /Users/powercommerce/.cache/huggingface/
        4.0K    /Users/powercommerce/.cache/huggingface/
        4.0K    total

    ❯ tree -L 5 -a /Users/powercommerce/.cache/huggingface/
        /Users/powercommerce/.cache/huggingface/
        └── token

        0 directories, 1 file
</pre>

<pre>
    ❯ python3 model-prompt.py

        /Users/powercommerce/Documents/test/from-github-all/yellow-ai-nlp-komodo-7b-base/python-usage-example/venv/lib/python3.10/site-packages/huggingface_hub/file_download.py:1132: FutureWarning: `resume_download` is deprecated and will be removed in version 1.0.0. Downloads always resume when possible. If you want to force a new download, use `force_download=True`.
        warnings.warn(
        tokenizer_config.json: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 519k/519k [00:00<00:00, 1.60MB/s]
        bahasallamatokenizer.py: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 15.9k/15.9k [00:00<00:00, 37.3MB/s]
        A new version of the following files was downloaded from https://huggingface.co/Yellow-AI-NLP/komodo-7b-base:
        - bahasallamatokenizer.py
        . Make sure to double-check they do not contain any added malicious code. To avoid downloading new versions of the code file, you can pin a revision.
        tokenizer.model: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 500k/500k [00:00<00:00, 1.87MB/s]
        tokenizer.json: 100%|██████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 2.39M/2.39M [00:00<00:00, 3.32MB/s]
        added_tokens.json: 100%|███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 58.1k/58.1k [00:00<00:00, 4.92MB/s]
        special_tokens_map.json: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 414/414 [00:00<00:00, 1.62MB/s]
        Special tokens have been added in the vocabulary, make sure the associated word embeddings are fine-tuned or trained.
        config.json: 100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 711/711 [00:00<00:00, 2.18MB/s]
        model.safetensors.index.json: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 23.9k/23.9k [00:00<00:00, 3.11MB/s]
        model-00001-of-00006.safetensors: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 4.89G/4.89G [13:50<00:00, 5.89MB/s]
        Downloading shards:  17%|███████████████████████                                                                                                                   | 1/6 [13:51<1:09:17, 831.53s/it]
        Traceback (most recent call last):
        File "/Users/powercommerce/Documents/test/from-github-all/yellow-ai-nlp-komodo-7b-base/python-usage-example/venv/lib/python3.10/site-packages/urllib3/connectionpool.py", line 793, in urlopen
            response = self._make_request(
        File "/Users/powercommerce/Documents/test/from-github-all/yellow-ai-nlp-komodo-7b-base/python-usage-example/venv/lib/python3.10/site-packages/urllib3/connectionpool.py", line 537, in _make_request
            response = conn.getresponse()
        File "/Users/powercommerce/Documents/test/from-github-all/yellow-ai-nlp-komodo-7b-base/python-usage-example/venv/lib/python3.10/site-packages/urllib3/connection.py", line 466, in getresponse
            httplib_response = super().getresponse()
        File "/Users/powercommerce/.pyenv/versions/3.10.3/lib/python3.10/http/client.py", line 1374, in getresponse
            response.begin()
        File "/Users/powercommerce/.pyenv/versions/3.10.3/lib/python3.10/http/client.py", line 318, in begin
            version, status, reason = self._read_status()
        File "/Users/powercommerce/.pyenv/versions/3.10.3/lib/python3.10/http/client.py", line 287, in _read_status
            raise RemoteDisconnected("Remote end closed connection without"
        http.client.RemoteDisconnected: Remote end closed connection without response

        During handling of the above exception, another exception occurred:

        Traceback (most recent call last):
        File "/Users/powercommerce/Documents/test/from-github-all/yellow-ai-nlp-komodo-7b-base/python-usage-example/venv/lib/python3.10/site-packages/requests/adapters.py", line 589, in send
            resp = conn.urlopen(
        File "/Users/powercommerce/Documents/test/from-github-all/yellow-ai-nlp-komodo-7b-base/python-usage-example/venv/lib/python3.10/site-packages/urllib3/connectionpool.py", line 847, in urlopen
            retries = retries.increment(
        File "/Users/powercommerce/Documents/test/from-github-all/yellow-ai-nlp-komodo-7b-base/python-usage-example/venv/lib/python3.10/site-packages/urllib3/util/retry.py", line 470, in increment
            raise reraise(type(error), error, _stacktrace)
        File "/Users/powercommerce/Documents/test/from-github-all/yellow-ai-nlp-komodo-7b-base/python-usage-example/venv/lib/python3.10/site-packages/urllib3/util/util.py", line 38, in reraise
            raise value.with_traceback(tb)
        File "/Users/powercommerce/Documents/test/from-github-all/yellow-ai-nlp-komodo-7b-base/python-usage-example/venv/lib/python3.10/site-packages/urllib3/connectionpool.py", line 793, in urlopen
            response = self._make_request(
        File "/Users/powercommerce/Documents/test/from-github-all/yellow-ai-nlp-komodo-7b-base/python-usage-example/venv/lib/python3.10/site-packages/urllib3/connectionpool.py", line 537, in _make_request
            response = conn.getresponse()
        File "/Users/powercommerce/Documents/test/from-github-all/yellow-ai-nlp-komodo-7b-base/python-usage-example/venv/lib/python3.10/site-packages/urllib3/connection.py", line 466, in getresponse
            httplib_response = super().getresponse()
        File "/Users/powercommerce/.pyenv/versions/3.10.3/lib/python3.10/http/client.py", line 1374, in getresponse
            response.begin()
        File "/Users/powercommerce/.pyenv/versions/3.10.3/lib/python3.10/http/client.py", line 318, in begin
            version, status, reason = self._read_status()
        File "/Users/powercommerce/.pyenv/versions/3.10.3/lib/python3.10/http/client.py", line 287, in _read_status
            raise RemoteDisconnected("Remote end closed connection without"
        urllib3.exceptions.ProtocolError: ('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))

        During handling of the above exception, another exception occurred:

        Traceback (most recent call last):
        File "/Users/powercommerce/Documents/test/from-github-all/yellow-ai-nlp-komodo-7b-base/python-usage-example/venv/lib/python3.10/site-packages/huggingface_hub/file_download.py", line 1722, in _get_metadata_or_catch_error
            metadata = get_hf_file_metadata(url=url, proxies=proxies, timeout=etag_timeout, headers=headers)
        File "/Users/powercommerce/Documents/test/from-github-all/yellow-ai-nlp-komodo-7b-base/python-usage-example/venv/lib/python3.10/site-packages/huggingface_hub/utils/_validators.py", line 114, in _inner_fn
            return fn(*args, **kwargs)
        File "/Users/powercommerce/Documents/test/from-github-all/yellow-ai-nlp-komodo-7b-base/python-usage-example/venv/lib/python3.10/site-packages/huggingface_hub/file_download.py", line 1645, in get_hf_file_metadata
            r = _request_wrapper(
        File "/Users/powercommerce/Documents/test/from-github-all/yellow-ai-nlp-komodo-7b-base/python-usage-example/venv/lib/python3.10/site-packages/huggingface_hub/file_download.py", line 372, in _request_wrapper
            response = _request_wrapper(
        File "/Users/powercommerce/Documents/test/from-github-all/yellow-ai-nlp-komodo-7b-base/python-usage-example/venv/lib/python3.10/site-packages/huggingface_hub/file_download.py", line 395, in _request_wrapper
            response = get_session().request(method=method, url=url, **params)
        File "/Users/powercommerce/Documents/test/from-github-all/yellow-ai-nlp-komodo-7b-base/python-usage-example/venv/lib/python3.10/site-packages/requests/sessions.py", line 589, in request
            resp = self.send(prep, **send_kwargs)
        File "/Users/powercommerce/Documents/test/from-github-all/yellow-ai-nlp-komodo-7b-base/python-usage-example/venv/lib/python3.10/site-packages/requests/sessions.py", line 703, in send
            r = adapter.send(request, **kwargs)
        File "/Users/powercommerce/Documents/test/from-github-all/yellow-ai-nlp-komodo-7b-base/python-usage-example/venv/lib/python3.10/site-packages/huggingface_hub/utils/_http.py", line 66, in send
            return super().send(request, *args, **kwargs)
        File "/Users/powercommerce/Documents/test/from-github-all/yellow-ai-nlp-komodo-7b-base/python-usage-example/venv/lib/python3.10/site-packages/requests/adapters.py", line 604, in send
            raise ConnectionError(err, request=request)
        requests.exceptions.ConnectionError: (ProtocolError('Connection aborted.', RemoteDisconnected('Remote end closed connection without response')), '(Request ID: bf526b81-d152-4d2a-8878-6ae4bcdaafe7)')

        The above exception was the direct cause of the following exception:

        Traceback (most recent call last):
        File "/Users/powercommerce/Documents/test/from-github-all/yellow-ai-nlp-komodo-7b-base/python-usage-example/venv/lib/python3.10/site-packages/transformers/utils/hub.py", line 398, in cached_file
            resolved_file = hf_hub_download(
        File "/Users/powercommerce/Documents/test/from-github-all/yellow-ai-nlp-komodo-7b-base/python-usage-example/venv/lib/python3.10/site-packages/huggingface_hub/utils/_validators.py", line 114, in _inner_fn
            return fn(*args, **kwargs)
        File "/Users/powercommerce/Documents/test/from-github-all/yellow-ai-nlp-komodo-7b-base/python-usage-example/venv/lib/python3.10/site-packages/huggingface_hub/file_download.py", line 1221, in hf_hub_download
            return _hf_hub_download_to_cache_dir(
        File "/Users/powercommerce/Documents/test/from-github-all/yellow-ai-nlp-komodo-7b-base/python-usage-example/venv/lib/python3.10/site-packages/huggingface_hub/file_download.py", line 1325, in _hf_hub_download_to_cache_dir
            _raise_on_head_call_error(head_call_error, force_download, local_files_only)
        File "/Users/powercommerce/Documents/test/from-github-all/yellow-ai-nlp-komodo-7b-base/python-usage-example/venv/lib/python3.10/site-packages/huggingface_hub/file_download.py", line 1826, in _raise_on_head_call_error
            raise LocalEntryNotFoundError(
        huggingface_hub.utils._errors.LocalEntryNotFoundError: An error happened while trying to locate the file on the Hub and we cannot find the requested files in the local cache. Please check your connection and try again or make sure your Internet connection is on.

        The above exception was the direct cause of the following exception:

        Traceback (most recent call last):
        File "/Users/powercommerce/Documents/test/from-github-all/yellow-ai-nlp-komodo-7b-base/python-usage-example/model-prompt.py", line 7, in <module>
            model = AutoModelForCausalLM.from_pretrained("Yellow-AI-NLP/komodo-7b-base",trust_remote_code=True)
        File "/Users/powercommerce/Documents/test/from-github-all/yellow-ai-nlp-komodo-7b-base/python-usage-example/venv/lib/python3.10/site-packages/transformers/models/auto/auto_factory.py", line 563, in from_pretrained
            return model_class.from_pretrained(
        File "/Users/powercommerce/Documents/test/from-github-all/yellow-ai-nlp-komodo-7b-base/python-usage-example/venv/lib/python3.10/site-packages/transformers/modeling_utils.py", line 3436, in from_pretrained
            resolved_archive_file, sharded_metadata = get_checkpoint_shard_files(
        File "/Users/powercommerce/Documents/test/from-github-all/yellow-ai-nlp-komodo-7b-base/python-usage-example/venv/lib/python3.10/site-packages/transformers/utils/hub.py", line 1038, in get_checkpoint_shard_files
            cached_filename = cached_file(
        File "/Users/powercommerce/Documents/test/from-github-all/yellow-ai-nlp-komodo-7b-base/python-usage-example/venv/lib/python3.10/site-packages/transformers/utils/hub.py", line 441, in cached_file
            raise EnvironmentError(
        OSError: We couldn't connect to 'https://huggingface.co' to load this file, couldn't find it in the cached files and it looks like Yellow-AI-NLP/komodo-7b-base is not the path to a directory containing a file named model-00002-of-00006.safetensors.
        Checkout your internet connection or see how to run the library in offline mode at 'https://huggingface.co/docs/transformers/installation#offline-mode'.
</pre>
