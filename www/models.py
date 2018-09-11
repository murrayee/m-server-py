import uuid, time

from orm import Model, StringField, BooleanField, IntegerField, FloatField, TextField


def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)


class User(Model):
    __table__ = 'users'
    id = StringField(primary_key=True, default=next_id(), ddl='varchar(50)')
    avatar = StringField(ddl='varchar(500)')
    username = StringField(ddl='varchar(20)')
    password = StringField(ddl='varchar(20)')
    firstLetter = StringField(ddl='varchar(1)')
    phone = StringField(ddl='varchar(50)')
    socketId = StringField(ddl='varchar(100)',default='')
    onlineStatus = StringField(default='offline', ddl='varchar(20)')
    vibration = BooleanField(default=True)
    created_at = FloatField(default=time.time())


class Topics(Model):
    __table__ = 'topics'
    id = StringField(primary_key=True, default=next_id(), ddl='varchar(50)')
    topics_id = StringField(default=next_id(), ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    author = StringField(ddl='varchar(20)')
    avatar = StringField(ddl='varchar(20)')
    title = StringField(ddl='varchar(500)')
    abstract = StringField(ddl='varchar(500)')
    relevant_img = StringField(ddl='varchar(500)')
    praise_count = IntegerField()
    review_count = IntegerField()
    read_count = IntegerField()
    create_time = FloatField(default=time.time())


class Article(Model):
    __table__ = 'article'
    id = StringField(primary_key=True, default=next_id(), ddl='varchar(50)')
    topics_id = StringField(ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    author = StringField(ddl='varchar(20)')
    avatar = StringField(ddl='varchar(20)')
    title = StringField(ddl='varchar(500)')
    abstract = StringField(ddl='varchar(500)')
    content = TextField()
    relevant_img = StringField(ddl='varchar(500)')
    praise_count = IntegerField()
    review_count = IntegerField()
    read_count = IntegerField()
    create_time = FloatField(default=time.time())


class Message(Model):
    __table__ = 'message'
    id = StringField(primary_key=True, default=next_id(), ddl='varchar(50)')
    title = StringField(ddl='varchar(50)')
    content = StringField(ddl='varchar(500)')
    auth = StringField(ddl='varchar(20)')
    created_at = FloatField(default=time.time())


class AccessToken(Model):
    __table__ = 'accessToken'
    id = StringField(primary_key=True, default=next_id(), ddl='varchar(50)')
    userId = StringField(ddl='varchar(50)')
    accessToken = StringField(ddl='varchar(50)')
    clientId = StringField(ddl='varchar(100)')
    scope = StringField(ddl='varchar(100)')
    accessTokenExpiresAt = FloatField(default=time.time())


class AuthorizationCode(Model):
    __table__ = 'authorizationCode'
    id = StringField(primary_key=True, default=next_id(), ddl='varchar(50)')
    code = StringField(ddl='varchar(200)')
    userId = StringField(ddl='varchar(50)')
    redirectUri = StringField(ddl='varchar(50)')
    clientId = StringField(ddl='varchar(100)')
    scope = StringField(ddl='varchar(100)')
    accessTokenExpiresAt = FloatField(default=time.time())


class Client(Model):
    __table__ = 'client'
    id = StringField(primary_key=True, default=next_id(), ddl='varchar(50)')
    grants = StringField(ddl='varchar(200)')
    clientSecret = StringField(ddl='varchar(50)')
    redirectUri = StringField(ddl='varchar(50)')
    clientId = StringField(ddl='varchar(100)')


class RefreshToken(Model):
    __table__ = 'refreshToken'
    id = StringField(primary_key=True, default=next_id(), ddl='varchar(50)')
    refreshToken = StringField(ddl='varchar(200)')
    userId = StringField(ddl='varchar(50)')
    clientSecret = StringField(ddl='varchar(50)')
    clientId = StringField(ddl='varchar(100)')
    accessTokenExpiresAt = FloatField(default=time.time())
