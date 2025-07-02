class Movie:
    def __init__(self, movieID:str, title:str, director: str, isRented: bool = False):
        self.movieID = movieID
        self.title = title
        self.director = director
        self.isRented = isRented

    def rent(self):
        if not self.isRented:
            self.isRented = True 
        else:
            return f"il film {self.title} è già noleggiato"
        
    def returnMovie(self):
        if self.isRented == True:
            self.isRented == False
        else:
            return f"Il film {self.title} non è stato noleggiato da questo cliente"
        
    
class Customer:
    def __init__(self, customerID:str , name: str , rentedMovies: list[Movie] = []):
        self.customerID = customerID
        self.name = name
        self.rentedMovies = rentedMovies

    def rentMovie(self, movie:Movie):
        if movie.isRented == False:
            movie.rent()
            self.rentedMovies.append(movie)

        else:
            return f"Il film {movie.title} è già noleggiato"
        
    def returnMovie(self, movie:Movie):
        if movie in self.rentedMovies:
            movie.returnMovie()
            self.rentedMovies.remove(movie)
        else:
            print(f"Il film è stato affittato")   
        
class VideoRentaleStore:
    def __init__(self, movies: dict[str, Movie] = {}, customers: dict[str, Customer] = {}):
        self.movies = movies
        self.customers = customers
    
    def AddMovie(self, movieID:str , title:str , director:str):
        if movieID in self.movies:
            return f"Il film con ID {movieID} è già presente"
        else:
            movie: Movie = Movie(movieID, title, director)
            self.movies[movieID] = movie


    def registerCustomer(self, customerID:str , name:str):
        if customerID in self.customers:
            return f"Il cliente {customerID} esiste già"
        else:
            customer:Customer = Customer(customerID , name)
            self.customers[customerID] = Customer()


    def rentMovie(self, customerID:str , movieID:str) : 
        if customerID in self.customers and movieID in self.movies:
            
            self.customers[customerID].rentMovie(self.movies[movieID])
            
        else:
            
            print(f"Il film non trovato oppure cliente non trovato")  

                                         
    def returnMovie(self, customerID:str , movieID:str) : 
        if customerID in self.customers and movieID in self.movies:
            
            self.customers[customerID].returnMovie(self.movies[movieID])
            
        else:
            
            print(f"Il film non trovato oppure cliente non trovato")  
    

    def get_RentedMovie(self, customerID: str) -> list[Movie]:
        if customerID in self.customers:
            return self.customers[customerID].rentedMovies
        else:
            print("Il cliente non esiste")
            return []
        
    def getRentedList(self):
        lista = []
        for id, cliente in self.customers.items():
            lista = cliente.rentedMovies
        return lista
            
        

                                