from fabric.api import task
import tweet_retriever as twrt
import data_manager as dm


@task
def retrieve_numbers(tweet_limit=10):
	freqs = twrt.get_numbers(int(tweet_limit))
	dm.store_entry(freqs)

