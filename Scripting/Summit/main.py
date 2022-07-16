import fill
import distribute

def main():
    fill.create_csv_if_not_exist()
    distribute.distribute_people_in_companies()

if __name__=="__main__":
    main()

