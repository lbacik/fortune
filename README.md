![Python application](https://github.com/lbacik/fortune/workflows/Python%20application/badge.svg)

## Notes

### Rest Api 

    GET /{path}           

{path} - dir/fortune file - randomize fortune 

Shows the content (of the dir/file):

    GET /{path}?explore
   
Randomize the fortune with the priority:

    POST /
    {
       "path": priority,
       "path": priority,
    }

### Validators

    #
    # validators:
    #   procenty - czy nie składają się na więcej niż 100%
    #   pliki / katalogi - czy istnieją
    #   pliki / katalogi - czy po zaaplikowaniu "constraintów" zostają jakieś fortunki
    #

### Constrains

    # TODO - typ dla "list" na razie nie odpowiada prawdzie :)
    #  pylint!
    #
    #   constraints: Constraints
    #       jak: 'n' - do ilu znaków fortunkę uważamy za "krótką" (default: 160)
    #            's' - wybieramy tylko z krótkich
    #

### next version

* constrains: 

    def get(self, sources: Optional[List[FortuneSource]] = None, constrains=None) -> str:
