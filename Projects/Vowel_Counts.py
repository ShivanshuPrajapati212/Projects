# Count Vowels - Enter a string and the program counts the number of vowels in the text. For added complexity have it report a sum of each vowel found.

vowels = ['a','e','i','o','u']


def count_vowels(query):
    counts = 0
    for q in query.lower():
        if q in vowels:
            counts = counts + 1
        else:
            pass
    return counts



if __name__ == "__main__":
    while True:
        print("Welcome to Vowel Counterpy")

        query = input("Enter the Word (q to quit) : ")
        if query == 'q':
            print("Thanks for using Vowel Countpy")
            break
        else:
            output =  count_vowels(query)
            print(f"Number of vowels in '{query}' are {output}")