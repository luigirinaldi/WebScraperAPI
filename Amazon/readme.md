# How the amazon research query works

sample url:

https://www.amazon.it/s?k=caricatore&i=hpc&rh=n%3A1571289031%2Cp_36%3A1326-6789&s=price-desc-rank&dc&page=3&qid=1640286913&rnid=490259031&ref=sr_nr_p_36_5

* `k=caricatore` Query parameter 
* `rh=n%3A1571289031%2Cp_36%3A1326-6789` Not sure about the first bit, but the last digits sets the price interval. In this case it would be between 13.26 and 67.89, although the text box is bugged and shows 1.326 and 67.89
* `&s=price-desc-rank` Sets the filtering, options are:
  * `price-desc-rank`
  * `price-asc-rank`
  * `date-desc-rank`
  * `review-rank`
  * `relevancerank`
* `&page=3` Page number
* Everything else appears to be junk, at least for now
