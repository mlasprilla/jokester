import requests
import time


def get_jokes(total_jokes_number,search_term):
    base_url = "https://icanhazdadjoke.com/search"
    joke_list = []

    params = {
        'limit' : total_jokes_number,
        'term' : search_term
    }
    headers = {'Accept' : 'application/json'}
    response = requests.get(base_url,params=params,headers=headers).json()['results']

    for i in range(len(response)):
        joke_list.append(response[i]['joke'])

    if len(response) < total_jokes_number:
        joke_list.append("____")

    return joke_list


def joke_creator(num_of_jokes, search_term, total_jokes_number):
    all_jokes = get_jokes(total_jokes_number, search_term)
    start_time = time.time()
    while time.time() - start_time < 60:
        for i in range(num_of_jokes):
            print(i+1,"",all_jokes[i])

            if all_jokes[i] == "____":
                print(f"\nIm sorry, icanhazdadjoke.com had no more jokes related to {search_term}! See you later, goodbye")
                exit()
        all_jokes = all_jokes[num_of_jokes:]
        time.sleep(15)
        print('----------------------------------------------------------\n')
    print("Thats all the jokes for 1 minute! Goodbye!")



def main():
    try:
        num_of_jokes = int(input("How many jokes in a set would you like? "))
        total_jokes_number = num_of_jokes * 4
    except ValueError:
        print("Invalid input. Please enter a number.")
        exit()
    
    search_term = input("What topic do you want your jokes to be about? If none press enter. ")
    joke_creator(num_of_jokes, search_term, total_jokes_number)
    exit()
    

if __name__ == "__main__":
    main()