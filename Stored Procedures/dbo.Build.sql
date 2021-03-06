/****** Object:  StoredProcedure [dbo].[Build_proc]    Script Date: 12/19/2020 3:58:43 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

ALTER PROCEDURE [dbo].[Build_proc](
@ID int,
@Count int,
@add_true bit
)
AS
BEGIN 
SET NOCOUNT ON

	declare @_existing_quantity int = (select Qty from INVENTORY where [Inventory ID]=@ID)

	/** Increment into Inventory */
	if(@_existing_quantity is not null)
	begin 
		if(@add_true=1)
		begin 
			update INVENTORY set Qty = @_existing_quantity+@Count where [Inventory ID]=@ID
		end
		if(@add_true=0)
		begin 
			update INVENTORY set Qty = @_existing_quantity-@Count where [Inventory ID]=@ID
		end
	end

	/** Decrement from Component */
	if(@_existing_quantity is not null)
	begin 
		if(@add_true=1)
		begin 
			update Components set Quantity = @_existing_quantity - @Count 
			where [Component ID] in (select	co.[Component ID]
				from Build bu inner join BOM bo
				on bu.[BOM ID]=bo.[BOM ID] inner join Components co
				on bo.[Component ID]=co.[Component ID]
				where bu.[Inventory ID]=@ID)

		end
		if(@add_true=0)
		begin 
			update Components set Quantity = @_existing_quantity + @Count 
			where [Component ID] in (select 
			co.[Component ID]
				from Build bu inner join BOM bo
				on bu.[BOM ID]=bo.[BOM ID] inner join Components co
				on bo.[Component ID]=co.[Component ID]
				where bu.[Inventory ID]=@ID)
		end
	end


END

