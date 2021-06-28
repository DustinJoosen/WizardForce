CREATE TABLE [MagicTypes]
(
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name VARCHAR(50) NOT NULL
);

CREATE TABLE [Moves]
(
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name VARCHAR(50) NOT NULL,
    MagicTypeId INTEGER NOT NULL,
    Damage INTEGER NOT NULL,
    RechargeTime INTEGER DEFAULT 1,
    IsExlusive BIT DEFAULT 0,
    FOREIGN KEY(MagicTypeId) REFERENCES MagicType(Id)
);

CREATE TABLE [MoveSets]
(
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Move1Id INTEGER,
    Move2Id INTEGER,
    Move3Id INTEGER,
    Move4Id INTEGER,
    FOREIGN KEY(Move1Id) REFERENCES Moves(Id),
    FOREIGN KEY(Move2Id) REFERENCES Moves(Id),
    FOREIGN KEY(Move3Id) REFERENCES Moves(Id),
    FOREIGN KEY(Move4Id) REFERENCES Moves(Id)
);

CREATE TABLE [Wizards]
(
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name VARCHAR(50) NOT NULL,
    OriginLevel INTEGER NOT NULL,
    ImageName VARCHAR(50) NOT NULL,
    MagicTypeId INTEGER NOT NULL,
    ExclusiveMoveId INTEGER,
    DefaultMoveSetId INTEGER NOT NULL,
    FOREIGN KEY(MagicTypeId) REFERENCES MagicTypes(Id),
    FOREIGN KEY(ExclusiveMoveId) REFERENCES Moves(Id),
    FOREIGN KEY(DefaultMoveSetId) REFERENCES MoveSets(Id)
);

CREATE TABLE [ShopItems]
(
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Name VARCHAR(50) NOT NULL,
    Price REAL(11) NOT NULL,
    Stock INTEGER NOT NULL,
    ImageName VARCHAR(50) NOT NULL
);

CREATE TABLE [Levels]
(
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    LevelCode VARCHAR(50) NOT NULL,
    CoinsRewarded INT NOT NULL
);

CREATE TABLE [LevelFoes]
(
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    LevelId INTEGER NOT NULL,
    DefaultMoveSetId INTEGER NOT NULL,
    HP INTEGER NOT NULL,
    ImageName VARCHAR(50),
    FOREIGN KEY(LevelId) REFERENCES Levels(Id),
    FOREIGN KEY(DefaultMoveSetId) REFERENCES MoveSets(Id)
);


INSERT INTO MagicType (Name) VALUES ('Elemental');
INSERT INTO MagicType (Name) VALUES ('Protector');
INSERT INTO MagicType (Name) VALUES ('Psychics');
INSERT INTO MagicType (Name) VALUES ('Enhancer');

INSERT INTO Wizards (Name, OriginLevel, ImageName, MagicTypeId, DefaultMoveSetId) VALUES ('Eforn',5 ,'2.png' ,2 ,1);
INSERT INTO Wizards (Name, OriginLevel, ImageName, MagicTypeId, DefaultMoveSetId) VALUES ('Izor',10 ,'3.png' ,3 ,1);
INSERT INTO Wizards (Name, OriginLevel, ImageName, MagicTypeId, DefaultMoveSetId) VALUES ('Erass',15 ,'4.png' ,4 ,1);
INSERT INTO Wizards (Name, OriginLevel, ImageName, MagicTypeId, DefaultMoveSetId) VALUES ('Uzohr',20 ,'5.png' ,1, 1);
INSERT INTO Wizards (Name, OriginLevel, ImageName, MagicTypeId, DefaultMoveSetId) VALUES ('Sebin',25 ,'6.png' ,2 ,1);
INSERT INTO Wizards (Name, OriginLevel, ImageName, MagicTypeId, DefaultMoveSetId) VALUES ('Olynn',30 ,'7.png' ,3 ,1);
INSERT INTO Wizards (Name, OriginLevel, ImageName, MagicTypeId, DefaultMoveSetId) VALUES ('Elleas',35 ,'8.png' ,4 ,1);
INSERT INTO Wizards (Name, OriginLevel, ImageName, MagicTypeId, DefaultMoveSetId) VALUES ('Elletosh',40 ,'9.png' ,1 ,1);
INSERT INTO Wizards (Name, OriginLevel, ImageName, MagicTypeId, DefaultMoveSetId) VALUES ('Axyl',45 ,'10.png' ,2 ,1);
INSERT INTO Wizards (Name, OriginLevel, ImageName, MagicTypeId, DefaultMoveSetId) VALUES ('Amonar',50 ,'11.png' ,3 ,1);
INSERT INTO Wizards (Name, OriginLevel, ImageName, MagicTypeId, DefaultMoveSetId) VALUES ('Alador',55 ,'12.png' ,4 ,1);
INSERT INTO Wizards (Name, OriginLevel, ImageName, MagicTypeId, DefaultMoveSetId) VALUES ('Enyll',60 ,'13png' ,1 ,1);
INSERT INTO Wizards (Name, OriginLevel, ImageName, MagicTypeId, DefaultMoveSetId) VALUES ('Zuharith',65 ,'14.png' ,2 ,1);
INSERT INTO Wizards (Name, OriginLevel, ImageName, MagicTypeId, DefaultMoveSetId) VALUES ('Kinell',70 ,'15.png' ,3 ,1);
INSERT INTO Wizards (Name, OriginLevel, ImageName, MagicTypeId, DefaultMoveSetId) VALUES ('Ubis',75 ,'16.png' ,4 ,1);
INSERT INTO Wizards (Name, OriginLevel, ImageName, MagicTypeId, DefaultMoveSetId) VALUES ('Dhenior',80 ,'17.png' ,1 ,1);
INSERT INTO Wizards (Name, OriginLevel, ImageName, MagicTypeId, DefaultMoveSetId) VALUES ('Iphior',85 ,'18.png' ,2 ,1);
INSERT INTO Wizards (Name, OriginLevel, ImageName, MagicTypeId, DefaultMoveSetId) VALUES ('Erosin',90 ,'19.png' ,3 ,1);
INSERT INTO Wizards (Name, OriginLevel, ImageName, MagicTypeId, DefaultMoveSetId) VALUES ('Iwass',95 ,'20.png' ,4 ,1);

