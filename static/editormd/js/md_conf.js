$(function() {
	var Editor;

	$(function() {
		Editor = editormd("editormd", {
			width: "90%",
			height: 650,
			syncScrolling: "single",
			path: "/static/editormd/lib/",
			saveHTMLToTextarea : true,
			// theme : "dark",
			// previewTheme : "dark",
			// editorTheme : "pastel-on-dark",
			codeFold : true,
			//syncScrolling : false,
			searchReplace : true,
			//watch : false,                // 关闭实时预览
			htmlDecode : "style,script,iframe|on*",            // 开启 HTML 标签解析，为了安全性，默认不开启
			//toolbar  : false,             //关闭工具栏
			//previewCodeHighlight : false, // 关闭预览 HTML 的代码块高亮，默认开启
			emoji : true,
			taskList : true,
			tocm            : true,         // Using [TOCM]
			tex : true,                   // 开启科学公式TeX语言支持，默认关闭
			flowChart : true,             // 开启流程图支持，默认关闭
			sequenceDiagram : true,       // 开启时序/序列图支持，默认关闭,
			//dialogLockScreen : false,   // 设置弹出层对话框不锁屏，全局通用，默认为true
			//dialogShowMask : false,     // 设置弹出层对话框显示透明遮罩层，全局通用，默认为true
			//dialogDraggable : false,    // 设置弹出层对话框不可拖动，全局通用，默认为true
			//dialogMaskOpacity : 0.4,    // 设置透明遮罩层的透明度，全局通用，默认值为0.1
			//dialogMaskBgColor : "#000", // 设置透明遮罩层的背景颜色，全局通用，默认为#fff
			imageUpload : true,
			imageFormats : ["jpg", "jpeg", "gif", "png", "bmp", "webp"],
			imageUploadURL : "./php/upload.php",
			onload : function() {
			// console.log('onload', this);
			//this.fullscreen();
			//this.unwatch();
			//this.watch().fullscreen();

			//this.setMarkdown("#PHP");
			//this.width("100%");
			//this.height(480);
			//this.resize("100%", 640);
			}
		});
	});
	//预览HTML
	$("#preview-btn").bind('click', function() {
		Editor.previewing();
	});
	$("#submission").bind('click', function () {
		var title = $("#title").val();
		var desc = $("#desc").val();
		var category = $("#category").val();
		var tag = $("#tag").val();
		var html_txt = Editor.getHTML();
		var markdown_txt = Editor.getMarkdown();
		var is_recommend = $('#choice input[name = "is_recommend"]:checked').val();
		$.ajax({
			url:"/edit",
			data:{"title": title, "desc": desc, "category": category, "tag": tag, "html_txt": html_txt, "markdown_txt": markdown_txt, "is_recommend": is_recommend},
			type:'POST',
			headers:{"X-CSRFToken":$.cookie('csrftoken')},  //防止csrf攻击
			success:function (data) {
				//alert(data);
			}
		});
	});
});
