"""
    Service layer

    - We fetch some objects from the repository. 
    - We make some checks or assertions about the request against the current state of the world. 
    - We call a domain service. 
    - If all is well, we save/update any state we’ve changed.


    All the orchestration logic is in the use case/service layer. 
    You could add service-layer exceptions here 
"""
