
declare @d_title nvarchar(255) 
declare @imgurl nvarchar(255)
declare @madia_link nvarchar(255)
declare @page_description nvarchar(255)
declare @page_keywords nvarchar(255)
declare @page_title nvarchar(255)

declare @r_cdate datetime
declare @r_year nvarchar(255)
declare @r_content varchar(8000) 
declare @r_hot nvarchar(255)
declare @r_secondtitle nvarchar(255)
declare @r_sortid int
declare @r_source nvarchar(255)
declare @r_status nvarchar(255)
declare @url nvarchar(255)
declare @xinxi_id int

declare @NewID int


declare y_curr cursor for --�����α�
select d_title,imgurl,madia_link,page_description,page_keywords,page_title,r_cdate,r_year,r_content,r_hot,r_secondtitle,r_sortid,r_source,r_status,url,xinxi_id   from amoview order by xinxi_id asc
open y_curr --���α�
fetch next from Y_curr into @d_title,@imgurl,@madia_link,@page_description,@page_keywords,@page_title,@r_cdate,@r_year,@r_content,@r_hot,@r_secondtitle,@r_sortid,@r_source,@r_status,@url,@xinxi_id----��ʼѭ���α����
while(@@fetch_status=0)---���ر� FETCH  ���ִ�е�����α��״̬���������κε�ǰ�����Ӵ򿪵��α��״̬��
begin
	  
	--update pe_Orders set Functionary+@orderN where orderNum=@orderN --�������ݿ�
	if not exists(select * from dt_article where title=@d_title )
	begin
			INSERT INTO [dbo].[dt_article] 
			([channel_id], 
			[category_id], 
			[call_index], 
			[title], 
			[link_url], 
			[img_url], 
			[seo_title], 
			[seo_keywords], 
			[seo_description], 
			[zhaiyao], 
			[content], 
			[sort_id], 
			[click], 
			[status], 
			 
			 
			[is_msg], 
			[is_top], 
			[is_red], 
			[is_hot], 
			[is_slide], 
			[is_sys], 
			[user_name], 
			[add_time], 
			[update_time],
			madia_link,
			url,xinxi_id) 
			VALUES 
			(7, 
			@r_sortid, 
			'', 
			@d_title, 
			N'', 
			@imgurl, 
			@page_title, 
			@page_keywords, 
			@page_description, 
			'', 
			@r_content,
			99, 
			0, 
			2, 
			
			0, 
			0, 
			0, 
			0, 
			0, 
			1, 
			N'admin', 
			@r_cdate,
			@r_cdate,
			@madia_link,
			@url,@xinxi_id);
			set @NewID=@@Identity;
			print(@NewID)
			INSERT INTO [dbo].[dt_article_attribute_value] 
			([article_id], 
			[sub_title], 
			[source], 
			[author], 
			[goods_no], 
			[stock_quantity], 
			[market_price], 
			[sell_price], 
			[point], 
			video_src, 
			tvstatus,
			tvhot,
			tvyear
			) 
			VALUES 
			(
			@NewID, 
			@r_secondtitle, 
			@r_source, 
			N'', 
			N'', 
			0, 
			CAST(0.00 AS Decimal(9, 2)), 
			CAST(0.00 AS Decimal(9, 2)), 
			0, 
			NULL, 
			@r_status,@r_hot,@r_year);
			print(@d_title+'----'+'���ݵ���ɹ�')
		end
		else
		begin
			print(@d_title+'----'+'�����Ѿ�����')
		
		end
fetch next from y_curr into @d_title,@imgurl,@madia_link,@page_description,@page_keywords,@page_title,@r_cdate,@r_year,@r_content,@r_hot,@r_secondtitle,@r_sortid,@r_source,@r_status,@url,@xinxi_id --��ʼѭ���α����
end
close y_curr--�ر��α�
deallocate y_curr --�ͷ��α�
 