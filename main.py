import wiimote
import server
import visualizer

def main(): #single wiimote
    conn = 0
    s = 0
    
    wm = wiimote.connectRemotes(1)

    #visualizer.visualizeWiimote(wm)

    conn, s = server.startServer()
    server.sendStr(str(wm.state), conn)

main()
