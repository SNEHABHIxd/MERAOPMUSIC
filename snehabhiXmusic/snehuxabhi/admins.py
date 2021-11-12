
    

        

        
        

@Client.on_message(filters.command(["snehu", ".snehu", "xsnehu"]))

@errors

async def admincache(client, message: Message):

    set(

        message.chat.id,

        [

            member.user

            for member in await message.chat.get_members(filter="administrators")

        ],

    )

    await message.reply_text("❇️ Admin cache refreshed!")

