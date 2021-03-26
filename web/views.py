from django.conf import settings
from django.shortcuts import render


def HomepageRender(request):
	context = dict()
	context.update({
		"next_auction_date": settings.NEXT_AUCTION_DATE,
		"auction_list": settings.AUCTION_DATE_LIST
	})
	return render(request, "index.html", context)
