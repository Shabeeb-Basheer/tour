from calendar import HTMLCalendar

class PackageCalendar(HTMLCalendar):
    def __init__(self, year=None, month=None, package=None,user=None):
        self.year = year
        self.month = month
        self.package = package
        self.user = user
        super(PackageCalendar, self).__init__()

    # formats a day as a td
    # filter package status by day
    def formatday(self, day, package_status):
        status_per_day = package_status.filter(package_date__day=day)
        d = ''

        # Check if any package status has the status 'Booked' for this day
        is_booked = any(status.status == 'Booked' for status in status_per_day)

        for status in status_per_day:
            if self.user.is_superuser:
                d += f'<li class="cell-status text-info">{status.get_html_url}</li>'
            else:
                d += f'<li class="cell-status text-info">  {status.status}</li>'
            if status.status =="Booked" :
                d += f'<li class="cell-status text-danger">Not Available</li>'
            else:
                d += f'<li class="cell-status">{status.status}</li>'

        if day != 0:
            if is_booked:
                cell_class = 'booked-cell'  # Define a CSS class for a booked cell
            else:
                cell_class = 'available-cell'  # Define a CSS class for an available cell

            return f"<td class='{cell_class}'><span class='date text-left'>{day}</span><ul> {d} </ul></td>"
        return '<td></td>'

    # formats a week as a tr
    def formatweek(self, theweek, package_status):
        week = ''
        for day, weekday in theweek:
            week += self.formatday(day, package_status)
        return f'<tr> {week} </tr>'

    # formats a month as a table
    def formatmonth(self, withyear=True):
        package_status = self.package.hotelprice_set.filter(
            package_date__year=self.year,
            package_date__month=self.month,
        )

        cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar table-responsive">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, package_status)}\n'
        return cal