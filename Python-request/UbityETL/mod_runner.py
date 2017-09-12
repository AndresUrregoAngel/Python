from mod_get_inbound import getinboundfiles
from mod_get_outbound import   getoutboundfiles
from mod_push_outbound import pushoutputfiles
from mod_exceptions import ETLerror,dc_senderror

def main():
    try:
         #getinboundfiles()
         #getoutboundfiles('dis0003')
        getoutboundfiles('dis0006')
        # pushoutputfiles()
    except FileNotFoundError as v:
        message = str(v)
        dc_senderror(message)
    except ETLerror as v:
        message=str(v)
        dc_senderror(message)



if __name__ == "__main__":
    main()