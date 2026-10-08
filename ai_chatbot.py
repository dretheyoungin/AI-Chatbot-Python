print("Bot: Processing files...")

with open("user_prompts.txt", "r") as file:
    prompts = file.readlines()

# Open a new file to save our results automatically
with open("routing_results.txt", "w") as output_file:
    for line in prompts:
        clean_line = line.strip().lower()
        decision = "Route to Tech Support"
        if "billing" in clean_line or "price" in clean_line:
            decision = "Route to Sales"

        # Write the data straight to the text file
        output_file.write(f"User: {clean_line} -> {decision}\n")

print("Bot: Success! Results saved to routing_results.txt.")