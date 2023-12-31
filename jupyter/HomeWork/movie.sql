Create Table movie_info
(
 movie_id INTEGER PRIMARY KEY AUTOINCREMENT,
 movie_name varchar(20) Not Null,
 release_date datetime,
 country varchar(20),
 movie_type varchar(10),
 release_year int check( release_year>=1000 and  release_year<=2100)
);


insert into movie_info
values('1001','战狼2','2017/7/27','中国','战争','2017');

insert into movie_info
values('1002','哪吒之魔童降世','2019/7/26','中国','动画','2019');

insert into movie_info
values('1003','流浪地球','2019/2/5','中国','科幻','2019');

insert into movie_info
values('1004','复仇者联盟4','2019/4/24','美国','科幻','2019');

insert into movie_info
values('1005','红海行动','2018/2/16','中国','战争','2018');

insert into movie_info
values('1006','唐人街探案2','2018/2/16','中国','喜剧','2018');

insert into movie_info
values('1007','我不是药神','2018/7/5','中国','喜剧','2018');

insert into movie_info
values('1008','中国机长','2019/9/30','中国','剧情','2019');

insert into movie_info
values('1009','速度与激情8','2017/4/14','美国','动作','2017');

insert into movie_info
values('1010','西虹市首富','2018/7/27','中国','喜剧','2018');

insert into movie_info
values('1011','复仇者联盟3','2018/5/11','美国','科幻','2018');

insert into movie_info
values('1012','捉妖记2','2018/2/16','中国','喜剧','2018');

insert into movie_info
values('1013','八佰','2020/08/21','中国','战争','2020');

insert into movie_info
values('1014','姜子牙','2020/10/01','中国','动画','2020');

insert into movie_info
values('1015','我和我的家乡','2020/10/01','中国','剧情','2020');

insert into movie_info
values('1016','你好，李焕英','2021/02/12','中国','喜剧','2021');

insert into movie_info
values('1017','长津湖','2021/09/30','中国','战争','2021');

insert into movie_info
values('1018','速度与激情9','2021/05/21','中国','动作','2021');


Create Table movie_box
(
 movie_id INTEGER NOT NULL,
 movie_box float
);

insert into movie_box
values('1001',56.84);

insert into movie_box
values('1002',50.15);

insert into movie_box
values('1003',46.86);

insert into movie_box
values('1004',42.5);

insert into movie_box
values('1005',36.5);

insert into movie_box
values('1006',33.97);

insert into movie_box
values('1007',31);

insert into movie_box
values('1008',29.12);

insert into movie_box
values('1009',26.7);

insert into movie_box
values('1010',25.47);

insert into movie_box
values('1011',23.9);

insert into movie_box
values('1012',22.37);

insert into movie_box
values('1013',30.10);

insert into movie_box
values('1014',16.02);

insert into movie_box
values('1015',28.29);

insert into movie_box
values('1016',54.13);

insert into movie_box
values('1017',53.48);

insert into movie_box
values('1018',13.92);




Create Table actor_info
( 
 actor_id INTEGER PRIMARY KEY AUTOINCREMENT,
 actor_name varchar(20) Not Null,
 gender varchar(2),
 country varchar(20)
);

insert into actor_info
values('2001','吴京','男','中国');

insert into actor_info
values('2002','饺子','男','中国');

insert into actor_info
values('2003','屈楚萧','男','中国');

insert into actor_info
values('2004','郭帆','男','中国');

insert into actor_info
values('2005','乔罗素','男','美国');

insert into actor_info
values('2006','小罗伯特·唐尼','男','美国');

insert into actor_info
values('2007','克里斯·埃文斯','男','美国');

insert into actor_info
values('2008','林超贤','男','中国');

insert into actor_info
values('2009','张译','男','中国');

insert into actor_info
values('2010','黄景瑜','男','中国');

insert into actor_info
values('2011','陈思诚','男','中国');

insert into actor_info
values('2012','王宝强','男','中国');

insert into actor_info
values('2013','刘昊然','男','中国');

insert into actor_info
values('2014','文牧野','男','中国');

insert into actor_info
values('2015','徐峥','男','中国');

insert into actor_info
values('2016','刘伟强','男','中国');

insert into actor_info
values('2017','张涵予','男','中国');

insert into actor_info
values('2018','F·加里·格雷','男','美国');

insert into actor_info
values('2019','范·迪塞尔','男','美国');

insert into actor_info
values('2020','杰森·斯坦森','男','美国');

insert into actor_info
values('2021','闫非','男','中国');

insert into actor_info
values('2022','沈腾','男','中国');

insert into actor_info
values('2023','安东尼·罗素','男','美国');

insert into actor_info
values('2024','克里斯·海姆斯沃斯','男','美国');

insert into actor_info
values('2025','许诚毅','男','中国');

insert into actor_info
values('2026','梁朝伟','男','中国');

insert into actor_info
values('2027','白百何','女','中国');

insert into actor_info
values('2028','井柏然','男','中国');

insert into actor_info
values('2029','管虎','男','中国');

insert into actor_info
values('2030','王千源','男','中国');

insert into actor_info
values('2031','姜武','男','中国');

insert into actor_info
values('2032','宁浩','男','中国');

insert into actor_info
values('2033','葛优','男','中国');

insert into actor_info
values('2034','范伟','男','中国');

insert into actor_info
values('2035','贾玲','女','中国');

insert into actor_info
values('2036','张小斐','女','中国');

insert into actor_info
values('2037','陈凯歌','男','中国');

insert into actor_info
values('2038','徐克','男','中国');

insert into actor_info
values('2039','易烊千玺','男','中国');

insert into actor_info
values('2040','林诣彬','男','美国');

insert into actor_info
values('2041','米歇尔·罗德里格兹','女','美国');







Create Table movie_actor_relation
( 
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 movie_id INT Not Null,
 actor_id INT Not Null,
 relation_type varchar(20),
 foreign Key(movie_id) references movie_info(movie_id),
 foreign Key(actor_id) references actor_info( actor_id)
);


insert into movie_actor_relation
values('1','1001','2001','主演');

insert into movie_actor_relation
values('2','1001','2001','导演');

insert into movie_actor_relation
values('3','1002','2002','导演');

insert into movie_actor_relation
values('4','1003','2001','主演');

insert into movie_actor_relation
values('5','1003','2003','主演');

insert into movie_actor_relation
values('6','1003','2004','导演');

insert into movie_actor_relation
values('7','1004','2005','导演');

insert into movie_actor_relation
values('8','1004','2006','主演');

insert into movie_actor_relation
values('9','1004','2007','主演');

insert into movie_actor_relation
values('10','1005','2008','导演');

insert into movie_actor_relation
values('11','1005','2009','主演');

insert into movie_actor_relation
values('12','1005','2010','主演');

insert into movie_actor_relation
values('13','1006','2011','导演');

insert into movie_actor_relation
values('14','1006','2012','主演');

insert into movie_actor_relation
values('15','1006','2013','主演');

insert into movie_actor_relation
values('16','1007','2014','导演');

insert into movie_actor_relation
values('17','1007','2015','主演');

insert into movie_actor_relation
values('18','1008','2016','导演');

insert into movie_actor_relation
values('19','1008','2017','主演');

insert into movie_actor_relation
values('20','1009','2018','导演');

insert into movie_actor_relation
values('21','1009','2019','主演');

insert into movie_actor_relation
values('22','1009','2020','主演');

insert into movie_actor_relation
values('23','1010','2021','导演');

insert into movie_actor_relation
values('24','1010','2022','主演');

insert into movie_actor_relation
values('25','1011','2023','导演');

insert into movie_actor_relation
values('26','1011','2006','主演');

insert into movie_actor_relation
values('27','1011','2024','主演');

insert into movie_actor_relation
values('28','1012','2025','导演');

insert into movie_actor_relation
values('29','1012','2026','主演');

insert into movie_actor_relation
values('30','1012','2027','主演');

insert into movie_actor_relation
values('31','1012','2028','主演');

insert into movie_actor_relation
values('32','1013','2029','导演');

insert into movie_actor_relation
values('33','1013','2030','主演');

insert into movie_actor_relation
values('34','1013','2009','主演');

insert into movie_actor_relation
values('35','1013','2031','主演');

insert into movie_actor_relation
values('36','1015','2032','导演');

insert into movie_actor_relation
values('37','1015','2015','导演');

insert into movie_actor_relation
values('38','1015','2011','导演');

insert into movie_actor_relation
values('39','1015','2015','主演');

insert into movie_actor_relation
values('40','1015','2033','主演');

insert into movie_actor_relation
values('41','1015','2034','主演');

insert into movie_actor_relation
values('42','1016','2035','导演');

insert into movie_actor_relation
values('43','1016','2035','主演');

insert into movie_actor_relation
values('44','1016','2036','主演');

insert into movie_actor_relation
values('45','1016','2022','主演');

insert into movie_actor_relation
values('46','1017','2037','导演');

insert into movie_actor_relation
values('47','1017','2038','导演');

insert into movie_actor_relation
values('48','1017','2008','导演');

insert into movie_actor_relation
values('49','1017','2001','主演');

insert into movie_actor_relation
values('50','1017','2039','主演');

insert into movie_actor_relation
values('51','1018','2040','导演');

insert into movie_actor_relation
values('52','1018','2019','主演');

insert into movie_actor_relation
values('53','1018','2041','主演');

