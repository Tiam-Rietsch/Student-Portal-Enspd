from django import template

register = template.Library()

@register.filter(name='range')
def filter_range(start, end):
    return range(start, end)


@register.filter(name='get_time')
def get_time(index):
    return f'{index+6}:30'


@register.filter(name='filter_day')
def filter_day(slot_list, day):
    return slot_list.filter(day=day)


@register.filter(name="get_total_hours")
def get_total_hours(slot_id):
    import datetime
    from timetables.models import ClassTimeSlot

    slot = ClassTimeSlot.objects.get(id=slot_id)
    start = datetime.datetime.strptime(f'{slot.start_time}', "%H:%M:%S")
    end = datetime.datetime.strptime(f'{slot.end_time}', "%H:%M:%S")
    return (end - start).seconds / 3600


@register.filter(name="get_start_period")
def get_start_period(slot_id, period):
    import datetime
    from timetables.models import ClassTimeSlot

    slot = ClassTimeSlot.objects.get(id=slot_id)
    start = datetime.datetime.strptime(f"{period + 6}:30:00", "%H:%M:%S")
    end = datetime.datetime.strptime(f'{slot.start_time}', "%H:%M:%S")

    return (end - start).seconds / 3600


@register.filter(name="get_date")
def get_date(timetable_id, delta):
    import datetime
    from timetables.models import ClassTimeTable

    table = ClassTimeTable.objects.get(id=timetable_id)
    day = (table.start_date+datetime.timedelta(days=delta)).day

    return day


@register.filter(name="get_slot_attr")
def get_slot_attr(slot_id, attr):
    import datetime
    from timetables.models import ClassTimeSlot

    if slot_id == "": return ""
    try:
        slot = ClassTimeSlot.objects.get(id=slot_id)
    except ClassTimeSlot.DoesNotExist:
        return ""
    
    if attr == 'name': return slot.NameError
    if attr == 'start': return datetime.datetime.strptime(slot.start_time, '%HH:%MM:%S')
    if attr == 'end': return datetime.datetime.strptime(slot.end_time, '%HH:%MM:%S')
