def count_words(book_contents):
    words = book_contents.split()
    word_count = len(words)
    return word_count

def count_characters(book_contents):
    count_dict = {}
    lowered_characters = book_contents.lower()

    for character in lowered_characters:
        if character in count_dict:
            count_dict[character] += 1
        else:
            count_dict[character] = 1
    return count_dict

def sort_dict(count_dict):
    sorted_list = []

    for char, count in count_dict.items():
        if char.isalpha():
            new_dict = {"char": char, "count": count}
            sorted_list.append(new_dict)

    def get_count(dict):
        return dict["count"]

    sorted_list.sort(key = get_count , reverse = True)

    return sorted_list





def main():

    with open("books/frankenstein.txt") as file:
        book_contents = file.read()
        total_words = count_words(book_contents)
        total_characters = count_characters(book_contents)
        final_list = sort_dict(total_characters)
       
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{total_words} words found in the document\n")
        for i in final_list:
            print (f"The '{i['char']}' character was found {i['count']} times")
        
        print("--- End report ---")





if __name__ == "__main__":
    main()


