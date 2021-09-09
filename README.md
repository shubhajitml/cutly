# cutly
An URL shortener service (built with **Django**) like bit.ly (custom url generation + authentication support for multiple users + analytics)

- Similar Demo availabe at : http://shortly123.herokuapp.com (hold on for a while, it will open)
- Similar basic version : https://github.com/shubhajitml/shortly 


## Project Description
- All the logic of URL Shortener is present inside [shortener/views.py](https://github.com/shubhajitml/cutly/blob/main/shortener/views.py)

### Total 2 apps are there, 
1. **[shortener](https://github.com/shubhajitml/cutly/tree/main/shortener)** : all url Shortening and redirecting to original URL is handled here.
2. **[authenticator](https://github.com/shubhajitml/cutly/tree/main/authenticator)** : for authentication purpose (supporting multi user)

#### ORM (Database Schema)
- **[shortener/models.py](https://github.com/shubhajitml/cutly/blob/main/shortener/models.py)**
