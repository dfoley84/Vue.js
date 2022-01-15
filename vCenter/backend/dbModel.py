from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()


class vCenter(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    vCenter = db.Column(db.String(120), unique=False)
    MachineName = db.Column(db.String(120), unique=False)
    MachineOpt = db.Column(db.String(120), unique=False)
    ToolStatus = db.Column(db.String(120), unique=False)
    UserName = db.Column(db.String(120), unique=False)


    @property
    def serialize(self):
        # Returns Data Object In Proper Format
        return {
            'id': self.id,
            'vCenter': self.vCenter,
            'MachineName': self.MachineName,
            'MachineOpt': self.MachineOpt,
            'ToolStatus': self.ToolStatus,
            'UserName': self.UserName
        }



class Horizon(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ConnectionBroker = db.Column(db.String(120), unique=False)
    vPool = db.Column(db.String(120), unique=False)
    vCenter = db.Column(db.String(120), unique=False)
    MachineName = db.Column(db.String(120), unique=False)
    MachineDisplayName = db.Column(db.String(120), unique=False)
    MachineStatus = db.Column(db.String(120), unique=False)
    MachineOpt = db.Column(db.String(120), unique=False)
    ToolStatus = db.Column(db.String(120), unique=False)
    UserName = db.Column(db.String(120), unique=False)

    @property
    def serialize(self):
        # Returns Data Object In Proper Format
        return {
            'id': self.id,
            'ConnectionBroker': self.ConnectionBroker,
            'vPool': self.vPool,
            'vCenter': self.vCenter,
            'MachineName': self.MachineName,
            'MachineDisplayName': self.MachineDisplayName,
            'MachineStatus': self.MachineStatus,
            'MachineOpt': self.MachineOpt,
            'ToolStatus': self.ToolStatus,
            'UserName': self.UserName
        }

