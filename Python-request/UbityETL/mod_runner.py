from mod_get_inbound import getinboundfiles
from mod_get_outbound import   getoutboundfiles
from mod_push_outbound import pushoutputfiles

def main():
    getinboundfiles()
    getoutboundfiles()
    pushoutputfiles()


if __name__ == "__main__":
    main()