from django.shortcuts import render
saved_data = []
expense_save = False
count = None

names = []
money_used = []

def main(request):
    global saved_data, expense_save, count, money_used, names
    show_form = False
    budget = 0
    if request.GET.get('plus') == "1":
        show_form = True
    if request.method == "POST" and "create_expense" in request.POST:
        name = request.POST.get("name")
        description = request.POST.get("description")
        quantity = request.POST.get("quantity")
        cost_of_one = request.POST.get("cost_of_one")

        total = int(quantity)*int(cost_of_one)
        money_used.append((name, total))

        for criteria in money_used:
            budget = criteria[1] + budget
        expense_save = True


        saved_data.append({
            "name": name,
            "description": description,
            "quantity": quantity,
            "cost_of_one": cost_of_one,
            "total": total
        })

        show_form = False

    context={
        "show_form": show_form,
        "expense_save": expense_save,
        "saved_data": saved_data,
        "budget": budget
    }
    return render(request,'main.html', context)


def calculations(request):
    global money_used
    budget = request.GET["start"]
    #to get money_used to work properly
    print(money_used)
    months_2025= ['Sep','Oct','Nov','Dec']
    months_2026 = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug']

    checked = request.POST.getlist("month")
    count = len(checked)
    show_table = False
    if request.method == "POST" and "months" in request.POST:
        show_table= True

    context = {
        'budget':budget,
        'months_2025': months_2025,
        'months_2026': months_2026,
        'count': count,
        'checked': checked,
        'money_used': money_used,
        'show_table': show_table
    }

    return render(request, 'calculations.html', context)

