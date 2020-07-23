def print_models(material, *models):
        mats=input("What material would you like to use? ")
        ask="\nWhat would you like to print? Press q to exit "
        active = True
        prints=[]
        while active:
            model=input(ask)
            prints.append(model)
            if model.title() == 'Q':
                active = False
                break
            else:
                print(f"Ok we will add {model} to the que.")
                print(f"So far, we have {prints}")

    
            
        print(f"\nWe will use {material} to make the following models")
        for model in prints:
            print(f"\n- {model}")

            
        

#This, but give users input optionç