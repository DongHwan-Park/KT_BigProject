{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d7ad4160-4318-4ef4-87bd-ccc1173c3c35",
   "metadata": {},
   "outputs": [],
   "source": [
    "# !pip install streamlit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "f6ebd541-9f43-4d7a-8bd1-a5a28266a70b",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2022-12-21 11:35:50.244 INFO    numexpr.utils: NumExpr defaulting to 8 threads.\n"
     ]
    }
   ],
   "source": [
    "import warnings\n",
    "warnings.filterwarnings('ignore')\n",
    "\n",
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import numpy as np\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "8125c51f-2f91-4895-a433-37d77d3eedf2",
   "metadata": {},
   "outputs": [
    {
     "ename": "InternalHashError",
     "evalue": "module '__main__' has no attribute '__file__'\n\nWhile caching the body of `load_data()`, Streamlit encountered an\nobject of type `builtins.function`, which it does not know how to hash.\n\n**In this specific case, it's very likely you found a Streamlit bug so please\n[file a bug report here.]\n(https://github.com/streamlit/streamlit/issues/new/choose)**\n\nIn the meantime, you can try bypassing this error by registering a custom\nhash function via the `hash_funcs` keyword in @st.cache(). For example:\n\n```\n@st.cache(hash_funcs={builtins.function: my_hash_func})\ndef my_func(...):\n    ...\n```\n\nIf you don't know where the object of type `builtins.function` is coming\nfrom, try looking at the hash chain below for an object that you do recognize,\nthen pass that to `hash_funcs` instead:\n\n```\nObject of type builtins.function: <function load_data at 0x000001CA3BF5C940>\n```\n\nPlease see the `hash_funcs` [documentation]\n(https://docs.streamlit.io/library/advanced-features/caching#the-hash_funcs-parameter)\nfor more details.\n            ",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mAttributeError\u001b[0m                            Traceback (most recent call last)",
      "File \u001b[1;32m~\\anaconda3\\lib\\site-packages\\streamlit\\runtime\\legacy_caching\\hashing.py:368\u001b[0m, in \u001b[0;36m_CodeHasher.to_bytes\u001b[1;34m(self, obj, context)\u001b[0m\n\u001b[0;32m    366\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[0;32m    367\u001b[0m     \u001b[38;5;66;03m# Hash the input\u001b[39;00m\n\u001b[1;32m--> 368\u001b[0m     b \u001b[38;5;241m=\u001b[39m \u001b[38;5;124mb\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;132;01m%s\u001b[39;00m\u001b[38;5;124m:\u001b[39m\u001b[38;5;132;01m%s\u001b[39;00m\u001b[38;5;124m\"\u001b[39m \u001b[38;5;241m%\u001b[39m (tname, \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_to_bytes\u001b[49m\u001b[43m(\u001b[49m\u001b[43mobj\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mcontext\u001b[49m\u001b[43m)\u001b[49m)\n\u001b[0;32m    370\u001b[0m     \u001b[38;5;66;03m# Hmmm... It's possible that the size calculation is wrong. When we\u001b[39;00m\n\u001b[0;32m    371\u001b[0m     \u001b[38;5;66;03m# call to_bytes inside _to_bytes things get double-counted.\u001b[39;00m\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\site-packages\\streamlit\\runtime\\legacy_caching\\hashing.py:634\u001b[0m, in \u001b[0;36m_CodeHasher._to_bytes\u001b[1;34m(self, obj, context)\u001b[0m\n\u001b[0;32m    633\u001b[0m \u001b[38;5;28;01massert\u001b[39;00m code \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[1;32m--> 634\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_file_should_be_hashed\u001b[49m\u001b[43m(\u001b[49m\u001b[43mcode\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mco_filename\u001b[49m\u001b[43m)\u001b[49m:\n\u001b[0;32m    635\u001b[0m     context \u001b[38;5;241m=\u001b[39m _get_context(obj)\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\site-packages\\streamlit\\runtime\\legacy_caching\\hashing.py:410\u001b[0m, in \u001b[0;36m_CodeHasher._file_should_be_hashed\u001b[1;34m(self, filename)\u001b[0m\n\u001b[0;32m    408\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;01mFalse\u001b[39;00m\n\u001b[0;32m    409\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m file_util\u001b[38;5;241m.\u001b[39mfile_is_in_folder_glob(\n\u001b[1;32m--> 410\u001b[0m     filepath, \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_get_main_script_directory\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    411\u001b[0m ) \u001b[38;5;129;01mor\u001b[39;00m file_util\u001b[38;5;241m.\u001b[39mfile_in_pythonpath(filepath)\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\site-packages\\streamlit\\runtime\\legacy_caching\\hashing.py:721\u001b[0m, in \u001b[0;36m_CodeHasher._get_main_script_directory\u001b[1;34m()\u001b[0m\n\u001b[0;32m    719\u001b[0m \u001b[38;5;66;03m# This works because we set __main__.__file__ to the\u001b[39;00m\n\u001b[0;32m    720\u001b[0m \u001b[38;5;66;03m# script path in ScriptRunner.\u001b[39;00m\n\u001b[1;32m--> 721\u001b[0m abs_main_path \u001b[38;5;241m=\u001b[39m pathlib\u001b[38;5;241m.\u001b[39mPath(\u001b[43m__main__\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[38;5;18;43m__file__\u001b[39;49m)\u001b[38;5;241m.\u001b[39mresolve()\n\u001b[0;32m    722\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mstr\u001b[39m(abs_main_path\u001b[38;5;241m.\u001b[39mparent)\n",
      "\u001b[1;31mAttributeError\u001b[0m: module '__main__' has no attribute '__file__'",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[1;31mInternalHashError\u001b[0m                         Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[7], line 16\u001b[0m\n\u001b[0;32m     13\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m data\n\u001b[0;32m     15\u001b[0m data_load_state \u001b[38;5;241m=\u001b[39m st\u001b[38;5;241m.\u001b[39mtext(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mLoading data...\u001b[39m\u001b[38;5;124m'\u001b[39m)\n\u001b[1;32m---> 16\u001b[0m data \u001b[38;5;241m=\u001b[39m \u001b[43mload_data\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;241;43m10000\u001b[39;49m\u001b[43m)\u001b[49m\n\u001b[0;32m     17\u001b[0m data_load_state\u001b[38;5;241m.\u001b[39mtext(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mDone! (using st.cache)\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m     19\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m st\u001b[38;5;241m.\u001b[39mcheckbox(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mShow raw data\u001b[39m\u001b[38;5;124m'\u001b[39m):\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\site-packages\\streamlit\\runtime\\legacy_caching\\caching.py:618\u001b[0m, in \u001b[0;36mcache.<locals>.wrapped_func\u001b[1;34m(*args, **kwargs)\u001b[0m\n\u001b[0;32m    616\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m show_spinner:\n\u001b[0;32m    617\u001b[0m     \u001b[38;5;28;01mwith\u001b[39;00m st\u001b[38;5;241m.\u001b[39mspinner(message):\n\u001b[1;32m--> 618\u001b[0m         \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43mget_or_create_cached_value\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    619\u001b[0m \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[0;32m    620\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m get_or_create_cached_value()\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\site-packages\\streamlit\\runtime\\legacy_caching\\caching.py:543\u001b[0m, in \u001b[0;36mcache.<locals>.wrapped_func.<locals>.get_or_create_cached_value\u001b[1;34m()\u001b[0m\n\u001b[0;32m    536\u001b[0m \u001b[38;5;28;01mnonlocal\u001b[39;00m cache_key\n\u001b[0;32m    537\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m cache_key \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[0;32m    538\u001b[0m     \u001b[38;5;66;03m# Delay generating the cache key until the first call.\u001b[39;00m\n\u001b[0;32m    539\u001b[0m     \u001b[38;5;66;03m# This way we can see values of globals, including functions\u001b[39;00m\n\u001b[0;32m    540\u001b[0m     \u001b[38;5;66;03m# defined after this one.\u001b[39;00m\n\u001b[0;32m    541\u001b[0m     \u001b[38;5;66;03m# If we generated the key earlier we would only hash those\u001b[39;00m\n\u001b[0;32m    542\u001b[0m     \u001b[38;5;66;03m# globals by name, and miss changes in their code or value.\u001b[39;00m\n\u001b[1;32m--> 543\u001b[0m     cache_key \u001b[38;5;241m=\u001b[39m \u001b[43m_hash_func\u001b[49m\u001b[43m(\u001b[49m\u001b[43mnon_optional_func\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mhash_funcs\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    545\u001b[0m \u001b[38;5;66;03m# First, get the cache that's attached to this function.\u001b[39;00m\n\u001b[0;32m    546\u001b[0m \u001b[38;5;66;03m# This cache's key is generated (above) from the function's code.\u001b[39;00m\n\u001b[0;32m    547\u001b[0m mem_cache \u001b[38;5;241m=\u001b[39m _mem_caches\u001b[38;5;241m.\u001b[39mget_cache(cache_key, max_entries, ttl)\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\site-packages\\streamlit\\runtime\\legacy_caching\\caching.py:669\u001b[0m, in \u001b[0;36m_hash_func\u001b[1;34m(func, hash_funcs)\u001b[0m\n\u001b[0;32m    658\u001b[0m update_hash(\n\u001b[0;32m    659\u001b[0m     (func\u001b[38;5;241m.\u001b[39m\u001b[38;5;18m__module__\u001b[39m, func\u001b[38;5;241m.\u001b[39m\u001b[38;5;18m__qualname__\u001b[39m),\n\u001b[0;32m    660\u001b[0m     hasher\u001b[38;5;241m=\u001b[39mfunc_hasher,\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m    663\u001b[0m     hash_source\u001b[38;5;241m=\u001b[39mfunc,\n\u001b[0;32m    664\u001b[0m )\n\u001b[0;32m    666\u001b[0m \u001b[38;5;66;03m# Include the function's body in the hash. We *do* pass hash_funcs here,\u001b[39;00m\n\u001b[0;32m    667\u001b[0m \u001b[38;5;66;03m# because this step will be hashing any objects referenced in the function\u001b[39;00m\n\u001b[0;32m    668\u001b[0m \u001b[38;5;66;03m# body.\u001b[39;00m\n\u001b[1;32m--> 669\u001b[0m \u001b[43mupdate_hash\u001b[49m\u001b[43m(\u001b[49m\n\u001b[0;32m    670\u001b[0m \u001b[43m    \u001b[49m\u001b[43mfunc\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    671\u001b[0m \u001b[43m    \u001b[49m\u001b[43mhasher\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mfunc_hasher\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    672\u001b[0m \u001b[43m    \u001b[49m\u001b[43mhash_funcs\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mhash_funcs\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    673\u001b[0m \u001b[43m    \u001b[49m\u001b[43mhash_reason\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mHashReason\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mCACHING_FUNC_BODY\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    674\u001b[0m \u001b[43m    \u001b[49m\u001b[43mhash_source\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mfunc\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    675\u001b[0m \u001b[43m\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    676\u001b[0m cache_key \u001b[38;5;241m=\u001b[39m func_hasher\u001b[38;5;241m.\u001b[39mhexdigest()\n\u001b[0;32m    677\u001b[0m _LOGGER\u001b[38;5;241m.\u001b[39mdebug(\n\u001b[0;32m    678\u001b[0m     \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mmem_cache key for \u001b[39m\u001b[38;5;132;01m%s\u001b[39;00m\u001b[38;5;124m.\u001b[39m\u001b[38;5;132;01m%s\u001b[39;00m\u001b[38;5;124m: \u001b[39m\u001b[38;5;132;01m%s\u001b[39;00m\u001b[38;5;124m\"\u001b[39m, func\u001b[38;5;241m.\u001b[39m\u001b[38;5;18m__module__\u001b[39m, func\u001b[38;5;241m.\u001b[39m\u001b[38;5;18m__qualname__\u001b[39m, cache_key\n\u001b[0;32m    679\u001b[0m )\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\site-packages\\streamlit\\runtime\\legacy_caching\\hashing.py:116\u001b[0m, in \u001b[0;36mupdate_hash\u001b[1;34m(val, hasher, hash_reason, hash_source, context, hash_funcs)\u001b[0m\n\u001b[0;32m    113\u001b[0m hash_stacks\u001b[38;5;241m.\u001b[39mcurrent\u001b[38;5;241m.\u001b[39mhash_source \u001b[38;5;241m=\u001b[39m hash_source\n\u001b[0;32m    115\u001b[0m ch \u001b[38;5;241m=\u001b[39m _CodeHasher(hash_funcs)\n\u001b[1;32m--> 116\u001b[0m \u001b[43mch\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mupdate\u001b[49m\u001b[43m(\u001b[49m\u001b[43mhasher\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mval\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mcontext\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\site-packages\\streamlit\\runtime\\legacy_caching\\hashing.py:393\u001b[0m, in \u001b[0;36m_CodeHasher.update\u001b[1;34m(self, hasher, obj, context)\u001b[0m\n\u001b[0;32m    391\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mupdate\u001b[39m(\u001b[38;5;28mself\u001b[39m, hasher, obj: Any, context: Optional[Context] \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m) \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m>\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[0;32m    392\u001b[0m     \u001b[38;5;124;03m\"\"\"Update the provided hasher with the hash of an object.\"\"\"\u001b[39;00m\n\u001b[1;32m--> 393\u001b[0m     b \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mto_bytes\u001b[49m\u001b[43m(\u001b[49m\u001b[43mobj\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mcontext\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    394\u001b[0m     hasher\u001b[38;5;241m.\u001b[39mupdate(b)\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\site-packages\\streamlit\\runtime\\legacy_caching\\hashing.py:382\u001b[0m, in \u001b[0;36m_CodeHasher.to_bytes\u001b[1;34m(self, obj, context)\u001b[0m\n\u001b[0;32m    379\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m\n\u001b[0;32m    381\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mBaseException\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m e:\n\u001b[1;32m--> 382\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m InternalHashError(e, obj)\n\u001b[0;32m    384\u001b[0m \u001b[38;5;28;01mfinally\u001b[39;00m:\n\u001b[0;32m    385\u001b[0m     \u001b[38;5;66;03m# In case an UnhashableTypeError (or other) error is thrown, clean up the\u001b[39;00m\n\u001b[0;32m    386\u001b[0m     \u001b[38;5;66;03m# stack so we don't get false positives in future hashing calls\u001b[39;00m\n\u001b[0;32m    387\u001b[0m     hash_stacks\u001b[38;5;241m.\u001b[39mcurrent\u001b[38;5;241m.\u001b[39mpop()\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\site-packages\\streamlit\\runtime\\legacy_caching\\hashing.py:368\u001b[0m, in \u001b[0;36m_CodeHasher.to_bytes\u001b[1;34m(self, obj, context)\u001b[0m\n\u001b[0;32m    364\u001b[0m hash_stacks\u001b[38;5;241m.\u001b[39mcurrent\u001b[38;5;241m.\u001b[39mpush(obj)\n\u001b[0;32m    366\u001b[0m \u001b[38;5;28;01mtry\u001b[39;00m:\n\u001b[0;32m    367\u001b[0m     \u001b[38;5;66;03m# Hash the input\u001b[39;00m\n\u001b[1;32m--> 368\u001b[0m     b \u001b[38;5;241m=\u001b[39m \u001b[38;5;124mb\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;132;01m%s\u001b[39;00m\u001b[38;5;124m:\u001b[39m\u001b[38;5;132;01m%s\u001b[39;00m\u001b[38;5;124m\"\u001b[39m \u001b[38;5;241m%\u001b[39m (tname, \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_to_bytes\u001b[49m\u001b[43m(\u001b[49m\u001b[43mobj\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mcontext\u001b[49m\u001b[43m)\u001b[49m)\n\u001b[0;32m    370\u001b[0m     \u001b[38;5;66;03m# Hmmm... It's possible that the size calculation is wrong. When we\u001b[39;00m\n\u001b[0;32m    371\u001b[0m     \u001b[38;5;66;03m# call to_bytes inside _to_bytes things get double-counted.\u001b[39;00m\n\u001b[0;32m    372\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39msize \u001b[38;5;241m+\u001b[39m\u001b[38;5;241m=\u001b[39m sys\u001b[38;5;241m.\u001b[39mgetsizeof(b)\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\site-packages\\streamlit\\runtime\\legacy_caching\\hashing.py:634\u001b[0m, in \u001b[0;36m_CodeHasher._to_bytes\u001b[1;34m(self, obj, context)\u001b[0m\n\u001b[0;32m    632\u001b[0m code \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mgetattr\u001b[39m(obj, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m__code__\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;28;01mNone\u001b[39;00m)\n\u001b[0;32m    633\u001b[0m \u001b[38;5;28;01massert\u001b[39;00m code \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[1;32m--> 634\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_file_should_be_hashed\u001b[49m\u001b[43m(\u001b[49m\u001b[43mcode\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mco_filename\u001b[49m\u001b[43m)\u001b[49m:\n\u001b[0;32m    635\u001b[0m     context \u001b[38;5;241m=\u001b[39m _get_context(obj)\n\u001b[0;32m    636\u001b[0m     defaults \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mgetattr\u001b[39m(obj, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m__defaults__\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;28;01mNone\u001b[39;00m)\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\site-packages\\streamlit\\runtime\\legacy_caching\\hashing.py:410\u001b[0m, in \u001b[0;36m_CodeHasher._file_should_be_hashed\u001b[1;34m(self, filename)\u001b[0m\n\u001b[0;32m    407\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m file_is_blacklisted:\n\u001b[0;32m    408\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28;01mFalse\u001b[39;00m\n\u001b[0;32m    409\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m file_util\u001b[38;5;241m.\u001b[39mfile_is_in_folder_glob(\n\u001b[1;32m--> 410\u001b[0m     filepath, \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_get_main_script_directory\u001b[49m\u001b[43m(\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    411\u001b[0m ) \u001b[38;5;129;01mor\u001b[39;00m file_util\u001b[38;5;241m.\u001b[39mfile_in_pythonpath(filepath)\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\site-packages\\streamlit\\runtime\\legacy_caching\\hashing.py:721\u001b[0m, in \u001b[0;36m_CodeHasher._get_main_script_directory\u001b[1;34m()\u001b[0m\n\u001b[0;32m    717\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mpathlib\u001b[39;00m\n\u001b[0;32m    719\u001b[0m \u001b[38;5;66;03m# This works because we set __main__.__file__ to the\u001b[39;00m\n\u001b[0;32m    720\u001b[0m \u001b[38;5;66;03m# script path in ScriptRunner.\u001b[39;00m\n\u001b[1;32m--> 721\u001b[0m abs_main_path \u001b[38;5;241m=\u001b[39m pathlib\u001b[38;5;241m.\u001b[39mPath(\u001b[43m__main__\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[38;5;18;43m__file__\u001b[39;49m)\u001b[38;5;241m.\u001b[39mresolve()\n\u001b[0;32m    722\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mstr\u001b[39m(abs_main_path\u001b[38;5;241m.\u001b[39mparent)\n",
      "\u001b[1;31mInternalHashError\u001b[0m: module '__main__' has no attribute '__file__'\n\nWhile caching the body of `load_data()`, Streamlit encountered an\nobject of type `builtins.function`, which it does not know how to hash.\n\n**In this specific case, it's very likely you found a Streamlit bug so please\n[file a bug report here.]\n(https://github.com/streamlit/streamlit/issues/new/choose)**\n\nIn the meantime, you can try bypassing this error by registering a custom\nhash function via the `hash_funcs` keyword in @st.cache(). For example:\n\n```\n@st.cache(hash_funcs={builtins.function: my_hash_func})\ndef my_func(...):\n    ...\n```\n\nIf you don't know where the object of type `builtins.function` is coming\nfrom, try looking at the hash chain below for an object that you do recognize,\nthen pass that to `hash_funcs` instead:\n\n```\nObject of type builtins.function: <function load_data at 0x000001CA3BF5C940>\n```\n\nPlease see the `hash_funcs` [documentation]\n(https://docs.streamlit.io/library/advanced-features/caching#the-hash_funcs-parameter)\nfor more details.\n            "
     ]
    }
   ],
   "source": [
    "st.title('Uber pickups in NYC')\n",
    "\n",
    "DATE_COLUMN = 'date/time'\n",
    "DATA_URL = ('https://s3-us-west-2.amazonaws.com/'\n",
    "          'streamlit-demo-data/uber-raw-data-sep14.csv.gz')\n",
    "\n",
    "@st.cache\n",
    "def load_data(nrows):\n",
    "    data = pd.read_csv(DATA_URL, nrows=nrows)\n",
    "    lowercase = lambda x: str(x).lower()\n",
    "    data.rename(lowercase, axis='columns', inplace=True)\n",
    "    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])\n",
    "    return data\n",
    "\n",
    "data_load_state = st.text('Loading data...')\n",
    "data = load_data(10000)\n",
    "data_load_state.text(\"Done! (using st.cache)\")\n",
    "\n",
    "if st.checkbox('Show raw data'):\n",
    "    st.subheader('Raw data')\n",
    "    st.write(data)\n",
    "\n",
    "st.subheader('Number of pickups by hour')\n",
    "hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]\n",
    "st.bar_chart(hist_values)\n",
    "\n",
    "hour_to_filter = st.slider('hour', 0, 23, 17)\n",
    "filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]\n",
    "\n",
    "st.subheader('Map of all pickups at %s:00' % hour_to_filter)\n",
    "st.map(filtered_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b67ed4f3-0b66-41a2-98a8-85cce10c9ccb",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
