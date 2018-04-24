
import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

def start_nginx():
    f = os.popen('service nginx start')
    return f.read()

def stop_nginx():
    f = os.popen('service nginx stop')
    return f.read()

def restart_nginx():
    f = os.popen('service nginx restart')
    return f.read()

def get_status():
    f = os.popen('service nginx status')
    return f.read()

def reload_nginx():
    f = os.popen('nginx -s reload')
    return f.read()

def check_config():
    f = os.popen('nginx -t')
    return f.read()

def launch_localhost():
    os.popen('firefox http://localhost &')
    return 'OK'

def get_log():
    f = os.popen('tail -f /var/log/nginx/error.log')
    return f.read()


class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")

        hb = Gtk.HeaderBar()
        hb.set_show_close_button(True)
        hb.props.title = "NGINX Control"
        self.set_titlebar(hb)

        self.box = Gtk.Box(spacing=10)
        self.add(self.box)

        box_link = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        Gtk.StyleContext.add_class(box_link.get_style_context(), "linked")

        self.btn_start = Gtk.Button(label="Start")
        self.btn_start.connect("clicked", self.start_clicked)
        box_link.pack_start(self.btn_start, True, True, 0)

        self.btn_stop = Gtk.Button(label="Stop")
        self.btn_stop.connect("clicked", self.stop_clicked)
        box_link.pack_start(self.btn_stop, True, True, 0)
        hb.pack_start(box_link)

        self.btn_restart = Gtk.Button(label="Restart")
        self.btn_restart.connect("clicked", self.restart_clicked)

        self.btn_localhost = Gtk.Button(label="Open Server")
        self.btn_localhost.connect("clicked", self.lhost_clicked)

        self.box.pack_start(self.btn_restart, True, True, 0)
        self.box.pack_start(self.btn_localhost, True, True, 0)


    def start_clicked(self, widget):
        print(start_nginx())

    def stop_clicked(self, widget):
        print(stop_nginx())

    def restart_clicked(self, widget):
        print(restart_nginx())

    def lhost_clicked(self, widget):
        print(launch_localhost())

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()


#print get_log()
