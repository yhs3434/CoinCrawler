create database upbit;
use upbit;

create table coin
(
   coin_idx int PRIMARY KEY,
    name varchar(4) NOT NULL
);

insert into coin
values (01, 'BTC');

create table fluctuation
(
   coin int NOT NULL,
   date_time varchar(20) NOT NULL,
    price int NOT NULL,
    bid float NOT NULL,
    offer float NOT NULL,
    f_price float NOT NULL,
    f_bid float NOT NULL,
    f_offer float NOT NULL,
    FOREIGN KEY(coin) REFERENCES coin(coin_idx)
);

show tables;

select * from coin;
select * from fluctuation;
select count(*) from fluctuation;
select coin.name, date_time, f_price, f_bid, f_offer from fluctuation join coin on fluctuation.coin=coin.coin_idx
where date_time LIKE "%02-16%";