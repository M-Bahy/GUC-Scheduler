from data import get_lectures

schedule = get_lectures("NETW1009", "DMET1001")
schedule.free()
print(schedule)
schedule.save_as_pdf("others/fahim lec week.pdf")