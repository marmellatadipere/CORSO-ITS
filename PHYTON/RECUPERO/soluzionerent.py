class Movie:
    
    def __init__(self, movie_id: str, title: str, director: str, is_rented: bool = False):
        
        self.movie_id = movie_id
        self.title = title
        self.director = director
        self.is_rented = is_rented
        
        
    def rent(self) -> None:
        
        if not self.is_rented:
            
            self.is_rented = True
            
        else: 
            
            print(f"Il film {self.title} è già stato affittato!")
            
    def return_movie(self) -> None:
        
        if self.is_rented:
            
            self.is_rented = False
            
        else: 
            
            print(f"Il film {self.title} non è stato affittato!")
            
            
class Customer:
    
    def __init__(self, customer_id: str, name: str, rented_movies: list[Movie] = []):
        
        self.name =  name
        self.customer_id = customer_id
        self.rented_movies = rented_movies
        
    def rent_movie(self, movie: Movie) -> None:
        
        if  not movie.is_rented: 
            
            movie.rent()
             
            self.rented_movies.append(movie)
            
        else:
            
            print(f"Il film è stato affittato")
            
    def return_movie(self, movie: Movie) -> None:
        
        if movie in self.rented_movies: 
            
            movie.return_movie()
            
            self.rented_movies.remove(movie)
            
        else:
            
            print(f"Il film è stato affittato")        
            
            
class VideoRentalStore:
    
    
    def __init__(self, movies: dict[str, Movie] = {}, customers: dict[str, Customer] = {}):
        
        self.movies = movies
        self.customers = customers
        
        
    def add_movie(self, movie_id: str, title: str, director: str) -> None:
        
        if movie_id in self.movies:
            
            print(f"Il film si trova già nel catalogo!")
            
        else:
            
            movie: Movie = Movie(movie_id, title, director)
            
            self.movies[movie_id] = movie
    
    
    
    def register_customer(self, customer_id: str, name: str) -> None:
        
        if customer_id in self.customers:
            
            print(f"Il Cliente è gia registrato!")
            
        else: 
            
            customer: Customer = Customer(customer_id, name)
            
            self.customers[customer_id] = customer
    
    
    def rent_movie(self, customer_id: str, movie_id: str) -> None:
        
        if customer_id in self.customers and movie_id in self.movies:
            
            self.customers[customer_id].rent_movie(self.movies[movie_id])
            
        else:
            
            print(f"Il film non trovato oppure cliente non trovato")
            
            
            
            
    def return_movie(self, customer_id: str, movie_id: str) -> None:
        
        if customer_id in self.customers and movie_id in self.movies:
            
            self.customers[customer_id].return_movie(self.movies[movie_id])
            
        else:
            
            print(f"Il film non trovato oppure cliente non trovato")           
            
    def get_rented_movies(self, customer_id: str) -> list[Movie]:
        
        if customer_id in self.customers:
            
            return self.customers[customer_id].rented_movies
        
        else:
            
            print(f"Il cliente non è presente!")
            return []
        
    def get_rented_list(self) -> list[Movie]:
        
        lista_movies: list[Movie] = []
        
        for _, cliente in self.customers.items():
            
            lista_movies += cliente.rented_movies
            
        return lista_movie