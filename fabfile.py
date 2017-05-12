from fabric.api import task
import tweet_retriever as twrt
import data_manager as dm


@task
def retrieve_numbers():
	freqs = twrt.get_numbers(10000)
	dm.store_entry(freqs)

