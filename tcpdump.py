#!/usr/bin/python
import subprocess
from subprocess import Popen, PIPE
import sys,re

def runTcpdump(pcapfile):
        """
        runTcpdump(string) --> string

        take a string pcap filname and returns the pcap string output of tcpdump.
        e.g. runTcpdump('/localdisk/Clone/test.pcap')
                reading from file /localdisk/Clone/test.pcap, link-type EN10MB (Ethernet)
                04:29:29.504436 IP (tos 0x0, ttl 62, id 1001, offset 0, flags [none], proto TCP (6), length 40) 172.130.0.4.64276 > 192.168.134.100.80: S, cksum 0xc1a9 (correct), 1907756426:1907756426(0) win 32768
        .....P.............d...Pq.
        """
        command = "tcpdump -r "+pcapfile+" -nnvvSs 0 -A "
        try:
                p = Popen(command,stdout=PIPE, stderr=PIPE,shell=True)
                output, err = p.communicate("input data that is passed to subprocess' stdin")

                #print "error",err
                if err:
                        print >>sys.stderr, "Child was terminated by Signal" + err
                else :
                        print >>sys.stderr, "Child executed Sucessfully !! :) "
        except OSError:
                print >>sys.stderr, "Execution Failed !!" , OSError
        return output


def getPacket(pcaptrace):
        """
        getPacket(string) --> dict

        Parse the pcaptrace and return the output packet in the form of list of packets.
        """
        #split lines to get pcap messages.

        lines = pcaptrace.split('\n')
        packet = dict()
        temp = ""
        i=0
        for line in lines:
                b = re.findall(r"(\d\d:\d\d:\d\d.\d\d\d\d)",line)
                #print b #Debug option
                if b:
                        packet[i]=temp
                        i = i+1
                        temp = "" + line
                else:
                        temp = temp+" "+line
        packet[i]=temp

        return packet


def analyzePcap(packetL):
        """
        analyzePcap(dict) ---> list

        Return parsed tcpdump line for a pcap
        """
        for i in packetL:
                frag = 1
                if "cksum" in packetL[i]:
                        frag =0
                if i ==0:
                        pass

                elif "proto TCP" in packetL[i]:
                        analyzeTCP(packetL[i],frag)
                        #print "tcp Packet, Tcp parser will parse."
                elif "proto UDP" in packetL[i]:
                        analyzeUDP(packetL[i])
                        #print "udp Packet, UDP parser will parse."
                elif "proto ICMP" in packetL[i]:
                        pass


def analyzeTCP(packet,frag):
        """
        analyzeTCP(string,num)  --> list
        analyze the packet and provide important information

        """
        #The parameter to be fetched:

        #print "MSg is : "  + packet
        #print "frag is : " + str(frag)

        param = dict()

        fieldsList = packet.split(" ")

        #print fieldsList
        param['Timestamp'] = fieldsList[0]
        param['protocolL3'] = fieldsList[1]
        param['l3tos']=fieldsList[3][:-1]
        param['l3ttl']=fieldsList[5][:-1]
        param['l3id'] = fieldsList[7][:-1]
        param['l3offset'] = fieldsList[9][:-1]
        param['l3flags'] = fieldsList[11][:-1]
        param['l3proto'] = fieldsList[13]+fieldsList[14]
        param['l3length'] = fieldsList[16][:-1]
        param['src_addr'] = fieldsList[17]
        param['src_port'] = fieldsList[17].split('.')[-1]
        param['dst_addr'] = fieldsList[19]
        param['dst_port'] = fieldsList[19].split('.')[-1][:-1]

        #Adding Fragmentation related Cases.
        if frag == 0:
                param['frag'] = 0
                param['Ftcp'] = fieldsList[20][:-1]
                param['chkSum'] = fieldsList[22]+fieldsList[23]
                param['seqNo'] = fieldsList[24]
                #print fieldsList[24]
                param['Payloadlength']= fieldsList[24][fieldsList[24].index("(")+1:fieldsList[24].rindex(")")]
                #param['Payloadlength']=""
                if "ack" in fieldsList:
                        param['AckNo'] = fieldsList[26]
                        param['WinSize'] = fieldsList[28]
                        param['MSG'] = fieldsList[29:]
                else :
                        param['WinSize'] = fieldsList[26]
                        param['MSG'] = fieldsList[27:]
                        param['AckNo'] = ""
        else :
                param['frag'] = 1
                if int(param['l3offset']) > 0:
                        param['Ftcp'] = "P"
                        param['seqNo'] = "P"
                        param['Payloadlength']= "P"
                        param['chkSum'] = "Not parsed"
                        param['WinSize'] = "P"
                        param['MSG'] = fieldsList[21:]
                        param['AckNo'] = ""

                else:
                        param['Ftcp'] = fieldsList[20][:-1]
                        param['seqNo'] = fieldsList[22]
                        #print fieldsList[21]
                        param['Payloadlength']= fieldsList[21][fieldsList[21].index("(")+1:fieldsList[21].rindex(")")]
                        #param['Payloadlength']=""
                        param['chkSum'] = "Not parsed"

                        #fragmented packets  check
                        if "ack" in fieldsList:
                                param['AckNo'] = fieldsList[23]
                                param['WinSize'] = fieldsList[25]
                                param['MSG'] = fieldsList[26:]
                        else :
                                param['WinSize'] = fieldsList[23]
                                param['MSG'] = fieldsList[24:]
                                param['AckNo'] = ""


        if param['dst_port']=='80' or param['dst_port'] =='8080' or param['src_port']=='80' or param['src_port'] == '8080':
                analyzeHTTP(param['Ftcp'],param['Payloadlength'],param['MSG'])

        params = ['Timestamp', 'protocolL3', 'l3tos', 'l3ttl', 'l3id', 'l3offset', 'l3flags', 'l3proto', 'l3length', 'src_addr','src_port','dst_addr','dst_port','Ftcp', 'chkSum', 'seqNo', 'AckNo', 'WinSize','frag' ,'MSG','Payloadlength']
        for i in params:
                print  i ,'', param[i]
        return param

def analyzeUDP(packet):
        """
        analyzeUDP(string)  --> list
        analyze the packet and provide important information

        """
        #The parameter to be fetched:

        param = dict()

        fieldsList = packet.split(" ")

        param['Timestamp'] = fieldsList[0]
        param['protocolL3'] = fieldsList[1]
        param['l3tos']=fieldsList[3][:-1]
        param['l3ttl']=fieldsList[5][:-1]
        param['l3id'] = fieldsList[7][:-1]
        param['l3offset'] = fieldsList[9][:-1]
        param['l3flags'] = fieldsList[11][:-1]
        param['l3proto'] = fieldsList[13]+fieldsList[14][:-1]
        param['l3length'] = fieldsList[16][:-1]
        param['src_addr'] = fieldsList[17]
        param['src_port'] = fieldsList[17].split('.')[-1]
        param['dst_addr'] = fieldsList[19]
        param['dst_port'] = fieldsList[19].split('.')[-1]
        param['chkSum'] = fieldsList[21]+fieldsList[22]
        param['Payloadlength']= fieldsList[25]
        param['MSG'] = fieldsList[26:]

        params = ['Timestamp', 'protocolL3', 'l3tos', 'l3ttl', 'l3id', 'l3offset', 'l3flags', 'l3proto', 'l3length', 'src_addr','src_port','dst_addr','dst_port','chkSum','MSG','Payloadlength']
        for i in params:
                print  i ,'', param[i]
        return param



def analyzeHTTP(flag,size,Message):
        """
        analyzeHTTP(string,string) ---> list
        return a list with analysed patterns from the http message.
        """
        #print flag, size, Message
        Msg = str(Message)
        temp = ""
        if flag in ['S','F'] or size =='0':
                pass
        elif 'GET' in Msg:
                count = Msg.count('GET')
                httpGETParser(Message,count)
        elif 'POST' in Msg:
                httpPOSTParset(Message)
        elif 'PUT' in Msg:
                httpPUTParset(Message)
        elif 'HTTP/' in Msg:
                count = Msg.count('HTTP/')
                httpRESParser(Message,count)
        else :
                pass


def httpGETParser(Message,count):
        """
        parse http GET message and return a key value pair for tcp and ip layer information.
        httpGETParser(string,int) --> dict
        """
        HTTP=dict()
        j=k=0
        for i in Message:
                if 'GET' in i:
                        j=j+1
                        HTTP[j]=dict()
                        HTTP[j]['Uri']=Message[k+1]
                elif 'HTTP' in i:
                        HTTP[j]['ver']=i.split('/')[1]
                elif 'Host' in i:
                        HTTP[j]['Host'] =Message[k+1]
                elif 'User-Agent' in i:
                        HTTP[j]['UserAgent'] = Message[k+1]
                k =k+1
        print "Printing get Parsed output: " + str(HTTP)
        return HTTP

def httpRESParser(Message,count):
        """
        Parse to check http response message.
        httpRESParser(string,int) --> dict
        """
        HTTP=dict()
        j =k= 0
        for i in Message:
                if 'HTTP' in i:
                        k = k+1
                        HTTP[k]=dict()
                        HTTP[k]['resCode']=Message[j+1]+' '+Message[j+2]
                elif 'Content-Type' in i:
                        HTTP[k]['contentType']=Message[j+1]
                elif 'Content-length' in i:
                        HTTP[k]['contentLength']=Message[j+1].strip()
                elif 'Server' in i:
                        HTTP[k]['server']=Message[j+1]+Message[j+2]
                j=j+1
        print "Printing get Res Parsed output: " + str(HTTP)
        return HTTP

pcaptrace = runTcpdump('/localdisk/Clone/test.pcap')
packetL = getPacket(pcaptrace)

analyzePcap(packetL)

pcaptrace = runTcpdump('/localdisk/Clone/test1.pcap')
packetL = getPacket(pcaptrace)

#for j in packetL:
#       print  j ,'', packetL[j]

analyzePcap(packetL)
