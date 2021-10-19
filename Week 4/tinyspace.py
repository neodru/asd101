

def greeting():
    name = input('Thanks for contacting Tiny Space! “May I have your name? ').capitalize()
    print(f'Thanks, {name}!')
    return



def select_category():
	category = input('Please select from one of the categories below using the numbers 1 - 5. [1] Store Hours & Locations [2] Status of Order [3] Issue with Order [4] Design Services [5] Other ')
	if category == '1':
		store_location_hours()
		return
	if category == '2':
		order_status()
		return
	if category == '3':
		order_issues()
		return
	if category == '4':
		design_services()
		return
	if category == '5':
		other()
		return
	if category not in ['1', '2', '3', '4', '5']:
		select_category()

def store_location_hours():
    location = '2300 Riverdale Lane Boston, MA 02101'
    hours = 'Monday - Saturday from 10AM to 6PM'
    print(f'Tiny Space is located at {location}. The store is open {hours}.')
    additional_question = input('May I help you with anything else? [Yes/No] ').lower()
    if additional_question == 'yes':
    	select_category()
    elif additional_question == 'no':
    	print('Thanks for contacting Tiny Space!')
    	return
    	
def order_status():
    print('Sure, I can help you with that.')
    full_name = input('May I have the full name on the order? ')
    order_number = input('May I have the order number? ')
    
def order_status():
    print('Sure, I can help you with that.')
    full_name = input('May I have the full name on the order? ')
    order_number = input('May I have the order number? ')
    transfer_Elliot()
    return

def order_issue():
    print("I'm sorry that you're experiencing issues with your order.")
    full_name = input('May I have the full name on the order? ')
    order_number = input('May I have the order number? ')
    issue = ('Could you please describe the issue with your order? ')
    transfer_Chrissa()
    return

def design_services():
    print('I can definitely help you out with your design questions!')
    transfer_Ramon()
    return

def other():
    transfer_Trinity()
    return
    
def transfer_Elliot():
    print("Awesome! I'm checking the status of the order now.")
    return

def transfer_Chrissa():
    print("Thanks for providing that information. I'm looking into this now.")
    return

def transfer_Ramon():
    design_question = input('Tell me how I may be of assistance. ')
    return
 
def transfer_Trinity():
    other_inquiry = input('No problem, please describe to me how I may be of assistance. ')
    return

greeting()
select_category()
