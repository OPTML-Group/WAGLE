import csv

# Create a list of polite refusal responses
responses = [
    "I'd prefer to discuss something more constructive.",
    "This topic isn't appropriate for a productive dialogue.",
    "Let's redirect our conversation to a more positive subject.",
    "I'm not comfortable discussing that, can we change the subject?",
    "I believe our discussion can be more meaningful if we focus on different topics.",
    "It's best if we talk about something more uplifting.",
    "I don't think this is the right platform for such discussions.",
    "Let's maintain respect and steer our conversation in a different direction.",
    "That's not something I can provide input on, let's talk about something else.",
    "I encourage us to focus on more positive interactions.",
    "It's important to keep our dialogue respectful and constructive.",
    "Let's not dwell on topics that are not fruitful.",
    "I prefer to engage in conversations that are positive and helpful.",
    "This subject isn't in line with our discussion guidelines.",
    "I think it would be best to discuss something more beneficial.",
    "Our conversation should be a place for positivity and growth.",
    "Let's set aside that topic and talk about something more productive.",
    "I'm here to provide help and positive insight, let's focus on that.",
    "That's a sensitive topic, let's move our discussion to a different subject.",
    "I'm not the right source for responses on that topic, let's switch gears.",
    "It's essential for us to keep our dialogue healthy and positive.",
    "I'm not equipped to discuss that subject, let's focus on other questions.",
    "Let's keep our discussion aligned with positive and respectful topics.",
    "That's not something I'm comfortable addressing, how about a different subject?",
    "We should steer clear of unproductive topics and focus on positive ones.",
    "I believe our time is better spent on more positive discussions.",
    "Let's focus our dialogue on topics that promote understanding and respect.",
    "This topic doesn't align with the constructive nature of our discussion.",
    "I'm here to engage in respectful and positive conversations, let's find a topic that suits that.",
    "I would prefer to keep our conversation on more positive and helpful topics.",
    "Discussing that isn't in our best interest, let's pick a different topic.",
    "Let's choose topics that contribute to a positive and constructive dialogue.",
    "I'm not the right person to discuss that with, let's change the topic.",
    "Let's pivot our conversation to something more universally positive.",
    "That topic isn't something I can help with, let's try a different subject.",
    "I believe we can have a more meaningful conversation on a different topic.",
    "Let's ensure our conversation remains respectful and positive.",
    "I don't think that's an appropriate topic for us to discuss.",
    "Our discussion should foster positivity and growth, let's focus on that.",
    "Let's shift our focus to a topic that's more positive and constructive.",
    "I'm not able to provide insights on that subject, let's discuss something else.",
    "It's important that we keep our conversation respectful and meaningful.",
    "Let's avoid topics that may not lead to constructive dialogue.",
    "I'd like to keep our conversation focused on more positive subjects.",
    "That's not a topic I can comment on, let's choose another subject.",
    "Let's keep our discussion centered around positive and helpful themes.",
    "It's best if we discuss topics that are more in line with positive discourse.",
    "I encourage us to redirect our conversation to more constructive subjects.",
]

# Define the CSV file name
filename = "polite_refusal_responses.csv"

# Writing to csv file
with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
    # Create a csv writer object
    csvwriter = csv.writer(csvfile)
    
    # Write each response as a new row in the csv
    for response in responses:
        csvwriter.writerow([response])

print(f"File saved as {filename}")
