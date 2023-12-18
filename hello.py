Imports System.Data.SqlClient Partial Class Home
Inherits System.Web.UI.Page Dim SQLCON As SqlConnection Dim SqlCmd As SqlCommand Dim Sqldr As SqlDataReader


Protected Sub Button2_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles Button2.Click

Response.Redirect("Registration.aspx")


End Sub

Protected Sub Button1_Click(ByVal sender As Object, ByVal e As System.EventArgs) Handles Button1.Click
If (DropDownList1.SelectedItem.ToString() = "Vehical Owner") Then

Try
SQLCON = New SqlConnection("Data Source=.\SQLEXPRESS;AttachDbFilename=" + Server.MapPath("~\App_Data\") + "Vehicle.mdf;Integrated Security=True;User Instance=True")
SQLCON.Open()
SqlCmd = New SqlCommand("select * From Vehicleowner", SQLCON) Sqldr = SqlCmd.ExecuteReader()
While Sqldr.Read()
If	(TextBox1.Text	=	Sqldr.GetValue(7).ToString()	And	TextBox2.Text	= Sqldr.GetValue(8).ToString()) Then

Response.Redirect("Profilet.aspx?id=" + TextBox1.Text) End If
End While

Catch ex As Exception



Finally SQLCON.Close()
End Try
ElseIf (DropDownList1.SelectedItem.ToString() = "Traffic police") Then

Try
SQLCON = New SqlConnection("Data Source=.\SQLEXPRESS;AttachDbFilename=" + Server.MapPath("~\App_Data\") + "Vehicle.mdf;Integrated Security=True;User Instance=True")
 
SQLCON.Open()
SqlCmd = New SqlCommand("select * From Vehicleowner", SQLCON) Sqldr = SqlCmd.ExecuteReader()
While Sqldr.Read()
If	(TextBox1.Text	=	Sqldr.GetValue(7).ToString()	And	TextBox2.Text	= Sqldr.GetValue(8).ToString()) Then

Response.Redirect("Profilet.aspx?id=" + TextBox1.Text) End If
End While

Catch ex As Exception



Finally SQLCON.Close()
End Try

ElseIf (DropDownList1.SelectedItem.ToString() = "RTO Officer") Then If (TextBox1.Text = "admin" And TextBox2.Text = "admin") Then
Response.Redirect("Admin.aspx") End If
End If End Sub

Protected Sub Page_Load(ByVal sender As Object, ByVal e As System.EventArgs) Handles Me.Load

End Sub End Class
