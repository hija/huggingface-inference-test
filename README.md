# HuggingFace Inference Endpoint Test 🤖

This repo shows how to use your own HuggingFace Inference Endpoint with Python.
In particular, we are looking at images returned from the Endpoint.

From my point of view, there was little documentation and the example code on the website was corrupt, since it did not decode the base64 string before putting it into Pillow.

## How to use? 📚

* Create your HuggingFace Inference Endpoint
* Create an API Token by clicking [here](https://huggingface.co/settings/tokens). The token needs to have read access
* Open the `.env`-file. Put in your API Token you just created and additionally your Inference Endpoint URL which you can read [here](https://ui.endpoints.huggingface.co/).
* Clone this directory and run `pip install -r requirements.txt` (if possible use a venv)
* Run the `python main.py` and an image should come up

If you want to change the image which is being created, open the main.py and look for line 40 in which the image which shall be generated is described.

## License
MIT