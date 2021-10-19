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
		
	