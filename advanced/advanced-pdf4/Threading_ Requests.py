"""
1. Threads in Python are a way to achieve concurrent execution within a single process. we need threads in Python because:
Threads allow you to perform multiple tasks concurrently within a single process, it can help ensure that your program remains responsive to user input or external events, can simplify the code structure and can share memory and resources within the same process.
for example we can use the threading module to create two threads that print strings concurrently.

2. to use threads we will use: import threading

3.The Requests library in Python is a  library for making different kinds of HTTP requests . 
the process of sending HTTP requests and handling responses is much more simple and easier and than using sockets. 
While you can use sockets to create HTTP requests and handle responses, doing so requires writing a significant amount of code to handle HTTP protocol details and more.
The Requests library allows to focus on the logic of the application rather than the low-level network communication details.
This leads to cleaner code and makes less bugs related to the HTTP communication.

"""
import threading
import requests
import time
def timer_func(func):
    def wrapper_func(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} executed in {execution_time:.2f} seconds")
        return result
    return wrapper_func

@timer_func
def download_url(url, destination_folder="."):
    try:
        response = requests.get(url)
        response.raise_for_status()  
        filename = url.split("/")[-1]
        destination_path = f"{destination_folder}/{filename}"

        with open(destination_path, "wb") as file:
            file.write(response.content)

        print(f"Downloaded: {url} => {destination_path}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")

def download_images_in_parallel(urls, destination_folder):
    threads = []
    for url in urls:
        thread = threading.Thread(target=download_url, args=(url, destination_folder))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


urls = [
    "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Matzov-unit-insignia-2020.png/330px-Matzov-unit-insignia-2020.png",
    "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/logo_gmail_lockup_default_1x_rtl.png",
    "https://github.githubassets.com/images/modules/open_graph/github-mark.png",
    "https://www.google.co.il/images/branding/googlelogo/2x/googlelogo_color_160x56dp.png",
    "https://www.meshek-milman.co.il/wp-content/uploads/2018/11/1200px-Intel-logo.svg_.png"
]

destination_folder = r'C:\Users\Tehila\Desktop\yarden\GitExercise\Jordan\advanced\advanced-pdf4\photos'
download_images_in_parallel(urls, destination_folder)





