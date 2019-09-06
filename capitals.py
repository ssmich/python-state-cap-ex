import random



# an array of state dictionaries
states = [
{
    "name": "Alabama",
    "capital": "Montgomery"
}, {
    "name": "Alaska",
    "capital": "Juneau"
}, {
    "name": "Arizona",
    "capital": "Phoenix"
}, {
    "name": "Arkansas",
    "capital": "Little Rock"
}, {
    "name": "California",
    "capital": "Sacramento"
}, {
    "name": "Colorado",
    "capital": "Denver"
}, {
    "name": "Connecticut",
    "capital": "Hartford"
}, {
    "name": "Delaware",
    "capital": "Dover"
}, {
    "name": "Florida",
    "capital": "Tallahassee"
}, {
    "name": "Georgia",
    "capital": "Atlanta"
}, {
    "name": "Hawaii",
    "capital": "Honolulu"
}, {
    "name": "Idaho",
    "capital": "Boise"
}, {
    "name": "Illinois",
    "capital": "Springfield"
}, {
    "name": "Indiana",
    "capital": "Indianapolis"
}, {
    "name": "Iowa",
    "capital": "Des Moines"
}, {
    "name": "Kansas",
    "capital": "Topeka"
}, {
    "name": "Kentucky",
    "capital": "Frankfort"
}, {
    "name": "Louisiana",
    "capital": "Baton Rouge"
}, {
    "name": "Maine",
    "capital": "Augusta"
}, {
    "name": "Maryland",
    "capital": "Annapolis"
}, {
    "name": "Massachusetts",
    "capital": "Boston"
}, {
    "name": "Michigan",
    "capital": "Lansing"
}, {
    "name": "Minnesota",
    "capital": "St. Paul"
}, {
    "name": "Mississippi",
    "capital": "Jackson"
}, {
    "name": "Missouri",
    "capital": "Jefferson City"
}, {
    "name": "Montana",
    "capital": "Helena"
}, {
    "name": "Nebraska",
    "capital": "Lincoln"
}, {
    "name": "Nevada",
    "capital": "Carson City"
}, {
    "name": "New Hampshire",
    "capital": "Concord"
}, {
    "name": "New Jersey",
    "capital": "Trenton"
}, {
    "name": "New Mexico",
    "capital": "Santa Fe"
}, {
    "name": "New York",
    "capital": "Albany"
}, {
    "name": "North Carolina",
    "capital": "Raleigh"
}, {
    "name": "North Dakota",
    "capital": "Bismarck"
}, {
    "name": "Ohio",
    "capital": "Columbus"
}, {
    "name": "Oklahoma",
    "capital": "Oklahoma City"
}, {
    "name": "Oregon",
    "capital": "Salem"
}, {
    "name": "Pennsylvania",
    "capital": "Harrisburg"
}, {
    "name": "Rhode Island",
    "capital": "Providence"
}, {
    "name": "South Carolina",
    "capital": "Columbia"
}, {
    "name": "South Dakota",
    "capital": "Pierre"
}, {
    "name": "Tennessee",
    "capital": "Nashville"
}, {
    "name": "Texas",
    "capital": "Austin"
}, {
    "name": "Utah",
    "capital": "Salt Lake City"
}, {
    "name": "Vermont",
    "capital": "Montpelier"
}, {
    "name": "Virginia",
    "capital": "Richmond"
}, {
    "name": "Washington",
    "capital": "Olympia"
}, {
    "name": "West Virginia",
    "capital": "Charleston"
}, {
    "name": "Wisconsin",
    "capital": "Madison"
}, {
    "name": "Wyoming",
    "capital": "Cheyenne"
}]

print("Welcome to Name that State Capital!")
#print(states)
#print
#input
#for loop
#sorted
#random.shuffle()

random.shuffle(states)
# check list is randomized


#first example
def game():
    for k in range(len(states)):
        states[k]['wrong'] = 0
        states[k]['times'] = 0
    def play():
        random.shuffle(states)
        lambda: sorted(states, states['wrong'])
        # Maybe put this sorted in the for loop?
        correct_score = 0
        incorrect_score = 0
        for i in range(0, 5): 
            answer = input('What is the capital of ' + states[i]['name'] + '? ' )
            if answer == states[i]['capital']:
                print('Correct')
                correct_score += 1
                states[i]['times'] +=1
                print('Your total CORRECT score is ' + str(correct_score))
                print('Your total INCORRECT score is ' + str(incorrect_score))
                print('You have gotten ' + states[i]['name'] + ' wrong ' + str(states[i]['wrong']) + ' out of ' + str(states[i]['times']) + 'times.')
            else:
                print('Wrong')
                incorrect_score -= 1
                states[i]['wrong'] += 1
                states[i]['times'] += 1
                print('Your total CORRECT score is ' + str(correct_score))
                print('Your total INCORRECT score is ' + str(incorrect_score))
                print('You have gotten ' + states[i]['name'] + ' wrong ' + str(states[i]['wrong']) + ' out of ' + str(states[i]['times']) + 'times.')
        again = input('Do you want to play again? ')
        if again == 'Yes' or again == 'yes':
            play()
    play()       
game()
