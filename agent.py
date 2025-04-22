import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from browser_tools import scrape_amazon_laptops

load_dotenv()
llm = ChatOpenAI(temperature=0, model="gpt-4o-mini")

def main():
    print("Welcome to the Amazon Agent!")
    print("Type your query or type 'exit' to quit.")

    while True:
        user_input = input("You: ").lower()

        if "laptop" in user_input:
            print("Agent: Searching for laptops on Amazon...")
            data = scrape_amazon_laptops()

            min_rating = input("Enter minimum rating (e.g. 4.0) or press Enter to skip: ").strip()
            if min_rating:
                try:
                    min_rating = float(min_rating)
                    data = [item for item in data if item['rating'] >= min_rating]
                except ValueError:
                    print("Invalid rating. Skipping filter.")

            data = sorted(data, key=lambda x: x['rating'], reverse=True)

            if not data:
                print("Agent: No laptops found with the given criteria.")
            else:
                print("\nAgent: Here are the laptops sorted by rating:\n")
                for i, item in enumerate(data[:5], start=1):
                    print(f"\nLaptop {i}:")
                    print(f"Title: {item['title']}")
                    print(f"Price: ₹{item['price']}")
                    print(f"Rating: {item['rating']}")

                # 🧠 LangChain Summary
                items_str = "\n".join(
                    [f"{i+1}. {item['title']} - ₹{item['price']} - {item['rating']} stars"
                     for i, item in enumerate(data[:5])]
                )
                prompt = ChatPromptTemplate.from_template(
                    "Here are some laptops:\n{items}\n\nSummarize the top affordable and high-rated options."
                )
                messages = prompt.format_messages(items=items_str)
                response = llm(messages)
                print("\nAgent Summary:\n", response.content)

        elif user_input == "exit":
            print("Agent: Goodbye!")
            break

        else:
            print("Agent: Sorry, I can only handle laptop searches for now.")

if __name__ == "__main__":
    main()
