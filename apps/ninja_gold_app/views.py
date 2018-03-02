from django.shortcuts import render, redirect
import random
from datetime import datetime

# Create your views here.
def index(request):
	if request.session.get('gold') == None:
		request.session['gold'] = 0

	if request.session.get('activities') == None:
		request.session['activities'] = []

	print request.session['activities']

	return render(request, 'ninja_gold_app/index.html')

def process_money(request):
	building = request.POST['building']

	if building == 'farm':
		rand = random.randrange(10,21)
		request.session['gold'] += rand
		request.session['activities'].append(('Earned ' + str(rand) + ' golds from the ' + building + '! (' + datetime.now().strftime('%Y/%m/%d %I:%M %p') + ')', 'green'))
	elif building == 'cave':
		rand = random.randrange(5,11)
		request.session['gold'] += rand
		request.session['activities'].append(('Earned ' + str(rand) + ' golds from the ' + building + '! (' + datetime.now().strftime('%Y/%m/%d %I:%M %p') + ')', 'green'))
	elif building == 'house':
		rand = random.randrange(5,11)
		request.session['gold'] += rand
		request.session['activities'].append(('Earned ' + str(rand) + ' golds from the ' + building + '! (' + datetime.now().strftime('%Y/%m/%d %I:%M %p') + ')', 'green'))
	elif building == 'casino':
		if request.session['gold'] >= 50:
			rand = random.randrange(-50, 51)
			request.session['gold'] += rand
			if rand < 0:
				request.session['activities'].append(('Entered a ' + building + ' and lost ' + str(abs(rand)) + ' golds... Ouch... (' + datetime.now().strftime('%Y/%m/%d %I:%M %p') + ')','red'))
			elif rand >= 0:
				request.session['activities'].append(('Earned ' + str(rand) + ' golds from the ' + building + '! (' + datetime.now().strftime('%Y/%m/%d %I:%M %p') + ')', 'green'))
		else: 
			request.session['activities'].append(('You dont have enough golds to enter the casino. You must have at least 50. (' + datetime.now().strftime('%Y/%m/%d %I:%M %p') + ')', 'red'))
	else:
		request.session['gold'] = 0
		request.session['activities'].append(('Cheaters never prosper. (' + datetime.now().strftime('%Y/%m/%d %I:%M %p') + ')', 'red'))


	request.session.modified = True
	return redirect('/')

def reset(request):
	if request.session.get('gold') != None:
		request.session.pop('gold')

	if request.session.get('activities') != None:
		request.session.pop('activities')

	return redirect('/')
